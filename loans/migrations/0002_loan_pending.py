# Generated by Django 4.2.1 on 2023-07-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
