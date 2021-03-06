# Generated by Django 2.1.4 on 2019-01-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='nbAcces',
            field=models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL"),
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='urlLongue',
            field=models.URLField(unique=True, verbose_name='URL à réduire'),
        ),
    ]
