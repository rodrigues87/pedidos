from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco_compra = models.DecimalField(decimal_places=2, max_digits=6)
    preco_venda = models.DecimalField(decimal_places=2, max_digits=6)
    descricao = models.TextField()
    quantidade_em_estoque = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produtos"
