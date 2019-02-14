from django.shortcuts import render, get_object_or_404, redirect
from .forms import MiniURLForm
from .ChoixCode import generer
from .models import MiniURL

# Create your views here.
def raccourcir(request):
    """
    Formulaire permettant de raccourcir une URL
    """
    form = MiniURLForm(request.POST or None)

    if form.is_valid():
        urlLongue = form.cleaned_data['urlLongue']
        pseudo = form.cleaned_data['pseudo']

        mini_url = form.save(commit=False)

        mini_url.code = generer(6)
        mini_url.save()

        envoi = True

    return render(request, 'mini_url/raccourcir.html', locals())

def accueil(request):
    """Afficher les dernières URL"""

    url_raccourcies = MiniURL.objects.all().order_by('nbAcces').reverse()

    return render(request, 'mini_url/accueil.html', {'url_raccourcies': url_raccourcies})

def redirections(request, code):
    url = get_object_or_404(MiniURL, code=code)
    url.nbAcces += 1
    url.save()

    return redirect(url.urlLongue)
