from django.contrib import admin
from django.utils.text import Truncator

from .models import Categorie, Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('titre', 'contenu')
    """
    fields = ('titre', 'auteur', 'categorie', 'contenu')
    """

    fieldsets = (
        # Filedset 1 : meta-info (titre, auteur...)
        ('Général', {
            'classes': ['collapse',],
            'fields':('titre', 'slug', 'auteur', 'categorie'),
            'description' : 'Meta-donnée'
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('contenu',)
        }),

        # Fieldset 3 : info date
        ('Date de l\'article', {
            'classes' : ['collapse',],
            'fields':('date',),
            'description': 'Vous pouvez modifier la date de l\'article'
        }),
    )

    prepopulated_fields = {'slug': ('titre', ), }

    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(article.contenu).chars(40, truncate='...')
    #en-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
