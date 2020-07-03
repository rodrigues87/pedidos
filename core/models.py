from django.dispatch import receiver

from usuarios.models import User
from django.db import models

from produtos.models import Produto
from django.db.models.signals import pre_delete


class PedidoQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:

            produto = Produto.objects.get(id=obj.produto.id)

            produto.quantidade_em_estoque = produto.quantidade_em_estoque + obj.quantidade

            produto.save()

        super(PedidoQuerySet, self).delete(*args, **kwargs)


class Pedido(models.Model):
    objects = PedidoQuerySet.as_manager()

    nome = models.CharField(max_length=150)
    email = models.EmailField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    endereco = models.CharField(max_length=150)
    entregue = models.BooleanField(default=False)
    pago = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pedidos"

    def save(self, *args, **kwargs):
        #ADICIONANDO VARIAVEL TOTAL
        self.total = self.quantidade * self.produto.preco_venda

        #VERIFICAR SE O PEDIDO EXISTE
            #REMOVER DO ESTOQUE
        try:
            pedido = Pedido.objects.get(id=self.id)

            super(Pedido, self).save(*args, **kwargs)
        except Pedido.DoesNotExist:

            produto = Produto.objects.get(id=self.produto.id)

            produto.quantidade_em_estoque = produto.quantidade_em_estoque - self.quantidade

            produto.save()

        #VERIFICA SE O USUARIO DIGITADO EXISTE
            #CRIA USUARIO
        try:
            user = User.objects.get(email=self.email)

        except User.DoesNotExist:

            user = User.objects.create_user(email=self.email,
                                            password='Azmel2020',
                                            first_name=self.nome)

        super(Pedido, self).save(*args, **kwargs)



"""
    def delete(self, using=None, keep_parents=False):

        
"""
