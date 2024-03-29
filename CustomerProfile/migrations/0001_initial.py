# Generated by Django 4.2.1 on 2023-07-30 12:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('surname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('telephone1', models.CharField(max_length=100)),
                ('telephone2', models.CharField(max_length=100)),
                ('dateofbirth', models.DateTimeField(null=True)),
                ('nicnumber', models.CharField(max_length=100)),
                ('profileimage', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='images')),
                ('nicimagefront', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='nic_images')),
                ('nicimageback', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='nic_images')),
            ],
        ),
    ]
