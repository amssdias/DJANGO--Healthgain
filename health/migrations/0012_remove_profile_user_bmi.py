# Generated by Django 3.0.8 on 2020-12-28 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_auto_20201226_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_user',
            name='bmi',
        ),
    ]