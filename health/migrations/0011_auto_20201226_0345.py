# Generated by Django 3.0.8 on 2020-12-26 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_auto_20201226_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_user',
            name='favourite_foods',
            field=models.ManyToManyField(blank=True, related_name='users_fav_food', to='health.Main_food'),
        ),
    ]
