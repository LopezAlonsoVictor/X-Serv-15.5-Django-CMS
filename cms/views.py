from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Pages

FORMULARIO = '''
            <form action="" Method="POST">
            Introduce:<br>
            <input type="text" name="name" placeholder="name">
            <input type="text" name="page" placeholder="page"><br>
            <input type="submit" value="Enviar">
</form>
'''

@csrf_exempt
def barra(request):
    if request.method == "POST":
        nuevo = Pages(name=request.POST['name'],page=request.POST['page'])
        nuevo.save()
    lista = Pages.objects.all()
    respuesta = '<ul>'
    for page in lista:
        respuesta += '<li>' + page.name
    respuesta += "</ul>"
    respuesta += FORMULARIO
    return HttpResponse(respuesta)

def page(rquest, nombre):
    try:
        page = Pages.objects.get(name=nombre)
    except Pages.DoesNotExist:
        raise Http404("No existe")
    return HttpResponse(page.page)
