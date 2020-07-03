from django.contrib import admin

# Register your models here.
from aquisicao.models import Aquisicao


class AquisicaoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'preco', 'data']
    list_display_links = ['produto']


admin.site.register(Aquisicao, AquisicaoAdmin)
