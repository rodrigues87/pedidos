# Generated by Django 3.0.7 on 2020-06-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200620_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]