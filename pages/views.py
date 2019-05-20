from django.shortcuts import render
from .forms import ContactForm
def index(request):
    context = {'titre': "salut les copains","nom": "franck"}
    return render(request, "pages/index.html", context)
def pageif(request):
    context = {'age' : 19}
    return render(request, "pages/pageif.html", context)
def pagefor(request):
    context = {'Ma_liste':['franck, jon, jean']}

    return render(request,"pages/pagefor.html", context)



def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'pages/contact.html', locals())
