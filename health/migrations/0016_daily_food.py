# Generated by Django 3.0.8 on 2020-12-29 00:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0015_delete_daily_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('drink', 'drink'), ('food', 'food')], max_length=40)),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10000)])),
                ('date_consumed', models.DateField()),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='health.Main_food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumed_food', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
