from django.urls import path
from . import views

# otro comentario
urlpatterns = [
    path('', views.index, name="desafio"), # /desafio/
    path('<int:mes>',views.desafio_mensual_por_numero),
    path('<str:mes>',views.desafio_mensual, name="desafio-mensual"),
]
