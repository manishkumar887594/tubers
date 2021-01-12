# Generated by Django 3.1.5 on 2021-01-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/slider/%Y/')),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
