# Generated by Django 4.2.1 on 2023-07-20 08:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerProfile', '0005_alter_customerprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='images'),
        ),
    ]