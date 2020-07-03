from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', list_pedidos, name='list_pedidos'),
    path('create', create_pedido, name='create_pedido'),
    path('update/<int:id>', update_pedido, name='update_pedido'),
    path('delete/<int:id>', delete_pedido, name='delete_pedido'),
    path('solicitar', solicitacao, name='solicitacao'),


]
