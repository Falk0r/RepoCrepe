# Generated by Django 2.1.4 on 2018-12-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181214_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
    ]