from django.db import models

# Create your models here.

class Tag(models.Model):
    nome = models.CharField(max_length=256)

class Noticia(models.Model):
    titulo = models.CharField(max_length=256)
    descricao = models.TextField()
    imagem = models.TextField()
class TagNoticia(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Carrossel(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    imagem = models.TextField()
    titulo = models.CharField(max_length=256)
    descricao = models.TextField()
    link = models.CharField(max_length=256)
    alinhamento = models.CharField(max_length=256)