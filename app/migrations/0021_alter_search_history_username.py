# Generated by Django 4.0.4 on 2022-05-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_search_history_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_history',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]
