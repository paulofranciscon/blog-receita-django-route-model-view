from django.urls import path

# manipulacao de quais arquivos sera visualido
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita')
]