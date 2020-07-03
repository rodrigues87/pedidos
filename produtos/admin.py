from django.contrib import admin

# Register your models here.
from core.models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco_compra', 'preco_venda', 'quantidade_em_estoque']
    list_display_links = ['nome']


admin.site.register(Produto, ProdutoAdmin)
