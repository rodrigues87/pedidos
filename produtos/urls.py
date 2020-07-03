from django.contrib import admin
from django.urls import path
from produtos.views import *

urlpatterns = [
    path('', list_produtos, name='list_produtos'),
    path('create', create_produto, name='create_produto'),
    path('update/<int:id>', update_produto, name='update_produto'),
    path('delete/<int:id>', delete_produto, name='delete_produto'),

]
