# Generated by Django 3.2.13 on 2022-06-17 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0002_partnerrequestmodel_related_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerrequestmodel',
            name='slug',
        ),
    ]
