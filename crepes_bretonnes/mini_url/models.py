from django.db import models
from django.utils import timezone

# Create your models here.
class MiniURL(models.Model):
    urlLongue = models.URLField(unique=True, verbose_name='URL à réduire')
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
    pseudo = models.CharField(max_length=42)
    nbAcces = models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")

    class Meta:
        verbose_name = "Mini-URL"
        ordering = ['date']

    def __str__(self):
        return self.urlLongue
