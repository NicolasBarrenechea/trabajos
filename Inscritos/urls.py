
from django.urls import path
from . import views
from .views import ApiRest, ApiRestdetail

urlpatterns = [
    path('', views.index),
    path('crud/', views.crud),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('apirest/', ApiRest.as_view(), name='apirest'),
    path('apirest/<int:pk>/', ApiRestdetail.as_view(), name='apirestdetail'),

    path('cbw/', views.ListarInscritos.as_view()),
    path('cbw/<int:pk>', views.DetalleInscritos.as_view()),


]
