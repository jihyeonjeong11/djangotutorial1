# Generated by Django 3.1.3 on 2020-11-28 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
