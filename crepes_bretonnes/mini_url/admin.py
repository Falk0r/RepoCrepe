from django.contrib import admin
from .models import MiniURL

# Register your models here.

class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('urlLongue', 'code', 'date', 'pseudo', 'nbAcces')
    list_filter = ('pseudo',)
    date_hierarchy = ('date')
    ordering = ('date',)
    search_fields = ('urlLongue',)

admin.site.register(MiniURL, MiniURLAdmin)
