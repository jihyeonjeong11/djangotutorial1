# Generated by Django 3.1.3 on 2020-11-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]