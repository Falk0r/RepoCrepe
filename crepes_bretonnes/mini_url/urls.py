from django.urls import path
from . import views

urlpatterns = [
    path('raccourcir', views.raccourcir, name='raccourcir'),
    path('', views.accueil, name='accueil'),
    path('m/<code>', views.redirections, name='redirection'),

    ]
