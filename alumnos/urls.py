from django.urls import path

from alumnos.views.alumnos import AlumnosListView, AlumnoCreateView, AlumnoUpdateView, AlumnoDelete, \
    AlumnosCompletoListView
from alumnos.views.base import IndexView

app_name = 'alumnos'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('alumnos/list/', AlumnosListView.as_view(), name='alumnos_list'),
    path('alumnos/new/', AlumnoCreateView.as_view(), name='alumnos_new'),
    path('alumnos/edit/<int:pk>/', AlumnoUpdateView.as_view(), name='alumnos_edit'),
    path('alumnos/del/', AlumnoDelete.as_view(), name='alumnos_delete'),

    path('alumnos/lista/completa/', AlumnosCompletoListView.as_view(), name='alumnos_lista_completa')
]