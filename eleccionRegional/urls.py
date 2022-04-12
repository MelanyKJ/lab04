from django.urls import URLPattern, path
from .import views

app_name = "eleccionRegional"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:region_id>/', views.lista_candi, name='index'),
]

