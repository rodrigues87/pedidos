from django import forms
from .models import Pedido
from produtos.models import Produto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['email','nome','produto' ,'quantidade', 'endereco']
        #produtos = forms.ModelChoiceField(queryset=Produto.objects.all(), widget=forms.Select(attrs={'onchange': "myFunction();"}))

