# Generated by Django 3.0.8 on 2021-01-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0024_remove_main_food_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_food',
            name='picture',
            field=models.ImageField(default='food-1.jpg', null=True, upload_to='food-list'),
        ),
    ]
