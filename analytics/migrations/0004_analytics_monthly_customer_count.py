# Generated by Django 4.2.1 on 2023-07-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_analytics_calculated_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='monthly_customer_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
