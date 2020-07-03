from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from produtos.forms import ProdutoForm
from produtos.models import Produto


@login_required(redirect_field_name='pedidos/solicitar')
def list_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'site/produtos/listarProdutos.html', {'produtos': produtos})


@login_required(redirect_field_name='pedidos/solicitar')
def create_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_produtos')
    return render(request, 'site/produtos/produto-form.html', {'form': form})


@login_required(redirect_field_name='pedidos/solicitar')
def update_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('list_produtos')
    return render(request, 'site/produtos/produto-form.html', {'form': form, 'produto': produto})


@login_required(redirect_field_name='pedidos/solicitar')
def delete_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == "POST":
        print("delete produto post")
        produto.delete()
        return redirect('list_produtos')
    print("delete get")
    return render(request, 'site/popup/../templates/site/pedidos/confirm-pedido-delete.html', {'produto': produto})
