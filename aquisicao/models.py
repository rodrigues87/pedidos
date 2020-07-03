from django.db import models

from produtos.models import Produto


class Aquisicao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.produto.nome

    class Meta:
        verbose_name_plural = "Aquisições"

    def save(self, *args, **kwargs):

        try:
            aquisicao = Aquisicao.objects.get(id=self.id)

            super(Aquisicao, self).save(*args, **kwargs)

        except Aquisicao.DoesNotExist:

            produto = Produto.objects.get(id=self.produto.id)

            produto.quantidade_em_estoque = produto.quantidade_em_estoque + self.quantidade

            produto.save()

        super(Aquisicao, self).save(*args, **kwargs)