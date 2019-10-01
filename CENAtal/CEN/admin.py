from django.contrib import admin
from .models import Tag, TagNoticia, Noticia, Carrossel
# Register your models here.

admin.site.register(Tag)
admin.site.register(TagNoticia)
admin.site.register(Noticia)

admin.site.register(Carrossel)

