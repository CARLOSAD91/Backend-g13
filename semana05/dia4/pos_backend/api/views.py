from rest_framework.views import APIView
from rest_framework.response import Response


from .models import (
  Plato, Categoria, Mesa
)


from .serializers import (
  CategoriaSerializer, MesaSerializer, PlatoSerializer,CategoriaPlatosSerializer,
  PedidoSerializerPOST
)


class IndexView(APIView):
    
    def get(self, request):
        context = {
          'ok': True,
          'message': 'el servidor esta activo!'
        }
        return Response(context)

class CategoriaView(APIView):
    
    def get(self, request):
      dataCategorias = Categoria.objects.all()
      serCategoria = CategoriaSerializer(dataCategorias, many=True)
      
      context = {
        'ok': True,
        'content':serCategoria.data
      }
      
      return Response(context)
    
class MesaView(APIView):
    
    def get(self, request):
      dataMesa = Mesa.objects.all()
      serMesa = MesaSerializer(dataMesa, many=True)
      
      context = {
        'ok': True,
        'content': serMesa.data
      }
      
      return Response(context)
    
class PlatoView(APIView):
  
  def get(self, request):
    dataPlato = Plato.objects.all()
    serPlato = PlatoSerializer(dataPlato, many=True)
      
    context = {
      'ok': True,
      'content': serPlato.data
    }
      
    return Response(context)
  
    
        
class CategoriaPlatosView(APIView):
  
  def get(self, request, categoria_id):
    dataCategoria = Categoria.objects.get(pk=categoria_id)
    serCategoriaPlatos = CategoriaPlatosSerializer(dataCategoria)
    
    context = {
      'ok': True,
      'content': serCategoriaPlatos.data
    }
    
    return Response(context)
  
class PedidoView(APIView):
  
  def post(self,request):
    serPedido = PedidoSerializerPOST(data=request.data)
    serPedido.is_valid(raise_exception=True)
    serPedido.save()

    context = {
            'ok':True,
            'content':serPedido.data
        }
    return Response(context)