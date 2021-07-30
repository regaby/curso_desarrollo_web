from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

desafios = {
    'enero': 'Practica python!',
    'febrero': 'Haz ejercicio!',
    'marzo': 'Come menos carne.',
    'abril': 'Practica python!',
    'mayo': 'Haz ejercicio!',
    'junio': 'Come menos carne.',
    'julio': 'Practica python!',
    'agosto': 'Haz ejercicio!',
    'septiembre': 'Come menos carne.',
    'octubre': 'Practica python!',
    'noviembre': 'Haz ejercicio!',
    'diciembre': None,
}

def index(request):
    #return HttpResponse("""<h1>App desafios</h1>""")
    lista_meses = list(desafios.keys())
    print ('lista_meses', lista_meses)
    # meses = ''
    # for mes in lista_meses:
    #     meses += f'<li><a href="{mes}">{mes}</a></li>'
    # print ('meses', meses)
    # return HttpResponse(f'<ul>{meses}</ul>')
    return render(request, "desafios/index.html",{'lista_meses': lista_meses})

def desafio_mensual_por_numero(request, mes):
    lista_meses = list(desafios.keys())
    # TODO: validar que mes no sea mayor a 12
    reverse_path = reverse("desafio-mensual",args=[lista_meses[mes-1]])
    print ('reverse_path', reverse_path)
    return HttpResponseRedirect(lista_meses[mes-1])

def desafio_mensual(request, mes):
    print ('mes', mes)
    texto_desafio = ''
    try:
        #texto_desafio = desafios[mes]
        #texto_desafio = render_to_string("desafios/desafio.html")
        return render(request, "desafios/desafio.html", {'texto_desafio': desafios[mes], 'mes': mes})
    except:
        return HttpResponseNotFound('<h2>mes no implementado<h2>')
    return HttpResponse(f'<h1>{texto_desafio}</h1>')