# Generated by Django 3.0.7 on 2020-06-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pedido_solicitante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='solicitante',
            field=models.EmailField(max_length=254),
        ),
    ]