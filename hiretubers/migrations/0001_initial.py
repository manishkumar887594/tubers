# Generated by Django 3.1.5 on 2021-01-12 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiretuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('tuber_id', models.IntegerField()),
                ('tuber_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
