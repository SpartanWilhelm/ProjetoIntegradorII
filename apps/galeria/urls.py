from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_obra, editar_obra, deletar_obra, filtro, artwork_view, artist_search_view

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name="buscar"),
    path('nova-obra', nova_obra, name="nova_obra"),
    path('editar-obra/<int:foto_id>', editar_obra, name="editar_obra"),
    path('deletar-obra/<int:foto_id>', deletar_obra, name="deletar_obra"),
    path('filtro/<str:categoria>', filtro, name='filtro'),
    path('artwork/<str:artwork_id>/', artwork_view, name='artwork_view'),
    path('search_artists/', artist_search_view, name='artist_search_view'),
]