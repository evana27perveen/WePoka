# Generated by Django 3.2.13 on 2022-06-18 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_content', '0003_postlovereact_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyllabusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=300)),
                ('session', models.CharField(blank=True, max_length=100, null=True)),
                ('syllabus', models.FileField(upload_to='syllabuses')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
