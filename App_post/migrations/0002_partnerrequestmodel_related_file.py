# Generated by Django 3.2.13 on 2022-06-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerrequestmodel',
            name='related_file',
            field=models.FileField(blank=True, null=True, upload_to='project_info_files'),
        ),
    ]
