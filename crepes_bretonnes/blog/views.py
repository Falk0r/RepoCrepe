from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import Article, Contact, Categorie
from .forms import ContactForm, NouveauContactForm
from django.views.generic import TemplateView, ListView

# Create your views here.
def home(request):
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crèpes bretonnes ça tue des mouettes en plein vol ! </p>
    """)
def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requete de l'utilisateur)

    """
    if id_article > 100:
        raise Http404

    return HttpResponse(
        #"Vous avez demandé l'article n° {} !".format(id_article)
        '<h1>Mon article ici</h1>'
    )
def list_article(request):
    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("<h2>Vous êtes redirigé.</h2>")

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    return render(request, 'blog/addition.html', locals())
"""
def accueil(request):
    #Afficher tous les articles de notre blog
    articles = Article.objects.all() #Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})
"""
def lire(request, id, slug):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id, slug=slug)

    return render(request, 'blog/lire.html', {'article': article})

def contact(request):
    #Construire le formulaire, soit aevc les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)

    if form.is_valid():
        #Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        #Nous pourrions ici envoyer l'email grâce aux données
        # que nous venons de récuperer
        envoi = True
    # Quoiqu'il arrive, on affiche la page du formulaire
    return render(request, 'blog/contact.html', locals())

def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data['nom']
        contact.adresse = form.cleaned_data['adresse']
        contact.photo = form.cleaned_data['photo']
        contact.save()
        sauvegarde = True

    return render(request, 'blog/contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })

def voir_contacts(request):
    return render(
    request,
    'blog/voircontacts.html',
    {'contacts': Contact.objects.all()}
    )
"""
class FAQView(TemplateView):
    template_name = "blog/faq.html"
"""
class ListeArticles(ListView):
    model = Article
    context_object_name = "derniers_articles"
    template_name = 'blog/accueil.html'
    paginate_by = 5
    #queryset = Article.objects.filter(categorie__id=1)
    def get_queryset(self):
        return Article.objects.filter(categorie__id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(ListeArticles, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context
