
from django.shortcuts import render
from . models import AutorDB, FraseDB

def indexVIew(request):
    '''esto es la pagina princila'''

    object = AutorDB.objects.all().order_by('id')

    return render(request, "index.html", {"object":object})