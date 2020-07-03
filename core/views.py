from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import PedidoForm
from core.models import Pedido
from usuarios.views import administrador


@login_required(redirect_field_name='pedidos/solicitar')
def list_pedidos(request):
    if request.user.is_authenticated:
        pedidos = Pedido.objects.all()
        return render(request, 'site/pedidos/listarPedidos.html', {'pedidos': pedidos})
    return redirect('/pedidos/solicitar')


@login_required(redirect_field_name='pedidos/solicitar')
def create_pedido(request):
    form = PedidoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_pedidos')
    return render(request, 'site/pedidos/pedido-form.html', {'form': form})


@login_required(redirect_field_name='pedidos/solicitar')
def update_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        return redirect('list_pedidos')
    return render(request, 'site/pedidos/pedido-form.html', {'form': form, 'pedido': pedido})


def delete_pedido(request, id):
    pedido = Pedido.objects.get(id=id)

    if request.method == "POST":
        print("delete pedido post")
        pedido.delete()
        return redirect('list_pedidos')

    return render(request, 'site/pedidos/confirm-pedido-delete.html', {'pedido': pedido})


def solicitacao(request):
    form = PedidoForm(request.POST or None)

    if form.is_valid():
        pedido = form.save()
        return render(request, 'site/pedidos/agradecimentos.html', {'pedido': pedido})
    return render(request, 'site/pedidos/solicitacao.html', {'form': form})


def agradecimentos(request, id):
    pedido = Pedido.objects.get(id=id)
    return render(request, 'site/pedidos/agradecimentos.html', {'pedido': pedido})
