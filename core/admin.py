from django.contrib import admin

# Register your models here.
from core.models import Pedido


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['email', 'nome', 'produto', 'quantidade', 'entregue','pago', 'data']
    list_display_links = ['nome', 'produto']


admin.site.register(Pedido, PedidoAdmin)
