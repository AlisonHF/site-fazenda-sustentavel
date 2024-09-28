from django.urls import path
from app_telas import views

urlpatterns = [
    path('index/', views.index, name='index'),  # Página inicial
    path('ajustes/', views.ajustes, name='ajustes'),  # Página de ajustes
    path('suporte/', views.suporte, name='suporte'),  # Página de suporte
    path('como_usar/', views.como_usar, name='como_usar'),  # Página de como_usar
]

