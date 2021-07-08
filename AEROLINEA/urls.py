from django.urls import path, include
from . import views

app_name = "AEROLINEA"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:vuelo_id>', views.vuelo, name="vuelo"),
    path('vuelo_alta', views.vuelo_alta, name="vuelo_alta"),
    path('<int:vuelo_id>/vuelo_modificar', views.vuelo_modificar, name="vuelo_modificar"),
    path('<int:vuelo_id>/vuelo_eliminar', views.vuelo_eliminar, name="vuelo_eliminar"),
    path('<int:vuelo_id>/reserva', views.reserva, name="reserva")
]