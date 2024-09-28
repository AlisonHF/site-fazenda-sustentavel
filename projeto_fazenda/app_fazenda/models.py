from django.db import models



# Criação do nosso banco de dados usado para cadastrar os dados do solo
class Dados(models.Model):
    id = models.AutoField(primary_key=True)
    bloco = models.IntegerField()
    cultivo = models.TextField(max_length=255)
    ph = models.FloatField()
    umidade = models.FloatField()
    textura = models.TextField(max_length=255)
    data = models.DateField(auto_now_add=True)
    # id_usuario 

class Cultivo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    umidade_recomendado = models.FloatField()
    ph_recomendado = models.FloatField()
    texto_recomendacao = models.TextField(max_length=1200)
    imagem = models.CharField(max_length=1000, blank=True, null=True)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)  
    senha = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)  
    telefone = models.CharField(max_length=15) 
    def __str__(self):
        return self.nome 
    