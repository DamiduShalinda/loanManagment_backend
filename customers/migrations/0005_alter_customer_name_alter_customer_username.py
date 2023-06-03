# Generated by Django 4.2.1 on 2023-06-03 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(default=models.CharField(max_length=100, unique=True), max_length=100),
        ),
    ]