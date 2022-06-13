# Generated by Django 4.0.4 on 2022-05-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_videos_watched_search_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_history',
            name='username',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='videos_watched',
            name='username',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
