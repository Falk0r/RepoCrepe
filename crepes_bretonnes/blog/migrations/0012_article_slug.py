# Generated by Django 2.1.4 on 2018-12-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181218_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='les nouvelles crepes', max_length=100),
            preserve_default=False,
        ),
    ]