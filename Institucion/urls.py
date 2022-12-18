from django.urls import path
from . import views


urlpatterns = [
    path('institucion/', views.institucion_list),
    path('institucion/<int:id>', views.institucion_detail),

    

]
