# Generated by Django 5.1.1 on 2024-09-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_fazenda', '0002_plantio_alter_dados_ph_alter_dados_umidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantio',
            name='imagem',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
