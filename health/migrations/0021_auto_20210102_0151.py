# Generated by Django 3.0.8 on 2021-01-02 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0020_messages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='recipes',
            options={'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(max_length=300),
        ),
    ]
