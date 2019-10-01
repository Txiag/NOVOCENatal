from django.shortcuts import render
from .models import Noticia, Carrossel
# Create your views here.

def index(request):
    ultimas_noticias = Noticia.objects.all()[:6:-1]
    carrossel = Carrossel.objects.all()
    context = {"ultimas_noticias": ultimas_noticias, "carrossel": carrossel}
    return render(request, "index.html", context)