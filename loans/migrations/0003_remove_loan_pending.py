# Generated by Django 4.2.1 on 2023-08-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_loan_pending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='pending',
        ),
    ]