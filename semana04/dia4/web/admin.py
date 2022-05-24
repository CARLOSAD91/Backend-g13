from django.contrib import admin

# Register your models here.
from . models import Categorias, Productos,CLiente,Pedido,pedidoDetalle
admin.site.register(Categorias)
admin.site.register(Productos)
admin.site.register(CLiente)
admin.site.register(Pedido)
admin.site.register(pedidoDetalle)

