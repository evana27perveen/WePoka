# Generated by Django 3.2.13 on 2022-06-18 03:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_content', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoveReact',
            new_name='PodcastLoveReact',
        ),
    ]
