from multiprocessing.connection import Client
from django.shortcuts import render, redirect
from .models import Categorias, Productos
from .carrito import Cart

# Create your views here.
def index(request):
    request.session['titulo'] = "MODA DJANGO"
    listaProductos = Productos.objects.all()
    listaCategorias = Categorias.objects.all()
    context = {
        'productos': listaProductos,
        'categorias': listaCategorias
    }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    objProducto = Productos.objects.get(pk=producto_id)
    context = {
        'producto': objProducto
    }
    return render(request, 'producto.html', context)

def productosPorCategoria(request, categoria_id):
    objCategoria = Categorias.objects.get(pk = categoria_id)
    listProductos = objCategoria.productos_set.all()
    listaCategorias = Categorias.objects.all()
    context = {
        'productos': listProductos,
        'categorias': listaCategorias
    }
    return render(request, 'index.html', context)
######### CARRITO DE COMPRAS ##########################

from web.carrito import Cart

def carrito(request):
    return render(request,'carrito.html')

def agregarCarrito(request,producto_id):
    objProducto = Productos.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    """
    funcion que elimina un producto del carrito de compras
    """
    objProducto = Productos.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)
    return render(request,'carrito.html')

def limpiarCarrito(request):
    carritoProducto = Cart(request)
    carritoProducto.clear()
    return render(request,'carrito.html')

##################### LOGIN DE USUARIO #############################
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def loginUsuario(request):
    context = {}
    if request.method == 'POST':
        #login de usuarios
        dataUsuario = request.POST['usuario']
        dataPassword = request.POST['password']
        usuarioAuth = authenticate(username=dataUsuario, password=dataPassword)
        
        if usuarioAuth is not None:
            login(request, usuarioAuth)
            return redirect('/cuenta')
        else:
            context = {'error': 'Usuario o contraseña incorrectos'}
        
    return render(request,'login.html', context)

def crearUsuario(request):
    
    if  request.method == 'POST':
        
        dataUsuario = request.POST['nuevoUsuario']
        dataPassword = request.POST['nuevoPassword']
        
        nuevoUsuario = User.objects.create_user(username=dataUsuario, password=dataPassword)
        login(request, nuevoUsuario)
        
        return redirect('/cuenta')

from .form import ClienteForm
from .models import CLiente    

def cuentaUsuario(request):
    #buscar si existe el cliente usuario
    try:
        clienteEditar = CLiente.objects.get(usuario = request.user)
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos': request.user.last_name,
            'email': request.user.email,
            'direccion':clienteEditar.direccion,
            'telefono':clienteEditar.telefono,
            'usuario':request.user.username,
        }
    except:
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos': request.user.last_name,
            'email': request.user.email,
            'usuario':request.user.username,
        }
    
    frmCliente =  ClienteForm(dataCliente)
    
    context = {
        'frmCliente' : frmCliente
    }
    
    return render(request, 'cuenta.html', context)

def actualizarCliente(request):
    mensaje = ""
    if request.method == 'POST':
        frmCliente = ClienteForm(request.POST)
        if frmCliente.is_valid():
            dataCliente = frmCliente.cleaned_data

            #actualización de usuario
            actUsuario = User.objects.get(pk=request.user.id)
            actUsuario.first_name = dataCliente["nombre"]
            actUsuario.last_name = dataCliente["apellidos"]
            actUsuario.email = dataCliente["email"]
            actUsuario.save()

            try:
                actCliente = CLiente.objects.get(usuario = request.user)
                actCliente.direccion = dataCliente["direccion"]
                actCliente.telefono = dataCliente["telefono"]
                actCliente.save()
            except:
                nuevoCliente = CLiente()
                nuevoCliente.usuario = actUsuario
                nuevoCliente.direccion = dataCliente["direccion"]
                nuevoCliente.telefono = dataCliente["telefono"]
                nuevoCliente.save()
            
            mensaje = "DATOS ACTUALIZADOS CORRECTAMENTE"
        else:
            mensaje = "ERROR AL ACTUALIZAR LOS DATOS"

    context = {
        'mensaje':mensaje,
        'frmCliente':frmCliente
    }

    return render(request,'cuenta.html',context)


########### PEDIDOS ########################
from .models import Pedido,pedidoDetalle

def registrarPedido(request):
    if request.user.id is not None:
        #registra cabecera del pedido
        clientePedido = CLiente.objects.get(usuario=request.user)
        nuevoPedido = Pedido()
        nuevoPedido.cliente = clientePedido
        nuevoPedido.save()

        #registra detalle del pedido
        carritoPedido = request.session.get("cart")
        for key,value in carritoPedido.items():

            productoPedido = Productos.objects.get(pk=value["producto_id"])

            nuevoPedidoDetalle = pedidoDetalle()
            nuevoPedidoDetalle.pedido = nuevoPedido
            nuevoPedidoDetalle.producto = productoPedido
            nuevoPedidoDetalle.cantidad = int(value["cantidad"])
            nuevoPedidoDetalle.save()

        carrito = Cart(request)
        carrito.clear()

        return render(request,'gracias.html')

    else:
        return redirect('/login')



