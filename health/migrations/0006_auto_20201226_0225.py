# Generated by Django 3.0.8 on 2020-12-26 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20201226_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(upload_to='health/static/health/images'),
        ),
    ]
