# Generated by Django 3.0.7 on 2020-06-20 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('preco_compra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.TextField()),
                ('quantidade_em_estoque', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
