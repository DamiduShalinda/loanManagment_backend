# Generated by Django 4.2.1 on 2023-06-24 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0007_alter_loan_loan_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_number',
        ),
    ]