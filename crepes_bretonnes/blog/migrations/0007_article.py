# Generated by Django 2.1.4 on 2018-12-18 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181218_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
            ],
            options={
                'verbose_name': 'article',
                'ordering': ['date'],
            },
        ),
    ]