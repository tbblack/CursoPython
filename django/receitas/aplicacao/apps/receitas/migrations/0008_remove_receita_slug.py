# Generated by Django 4.0.3 on 2022-04-29 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0007_receita_slug_alter_categoria_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='slug',
        ),
    ]
