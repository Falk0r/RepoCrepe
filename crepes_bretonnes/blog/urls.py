from django.urls import path
from . import views
from django.views.generic import TemplateView, ListView
from .models import Article

urlpatterns = [
    path('accueil', views.home),
    #path('article/<int:id_article>', views.view_article),
    path('list_article', views.list_article),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    #path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.nouveau_contact, name='contact'),
    path('voir-contacts', views.voir_contacts, name='voir_contact'),
    #path('faq', views.FAQView.as_view()),
    path('faq', TemplateView.as_view(template_name='blog/faq.html')),
    path('', views.ListeArticles.as_view(), name='blog_liste'),
    path('categorie/<int:id>', views.ListeArticles.as_view(), name='blog_categorie'),

]
