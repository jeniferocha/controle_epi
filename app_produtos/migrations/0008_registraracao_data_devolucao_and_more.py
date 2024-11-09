# Generated by Django 5.1 on 2024-10-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_produtos", "0007_remove_registraracao_nome_colaborador_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="registraracao",
            name="data_devolucao",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="registraracao",
            name="observacao",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]