# Generated by Django 3.2.13 on 2022-06-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0004_auto_20220617_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostmodel',
            name='gender_specification',
            field=models.CharField(default='Not Specified', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobpostmodel',
            name='work_type',
            field=models.CharField(max_length=100),
        ),
    ]