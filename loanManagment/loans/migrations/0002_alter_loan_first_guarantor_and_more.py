# Generated by Django 4.2.1 on 2023-07-12 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerProfile', '0001_initial'),
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='first_guarantor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_guarantor', to='CustomerProfile.customerprofile'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='second_guarantor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_guarantor', to='CustomerProfile.customerprofile'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CustomerProfile.customerprofile'),
        ),
    ]
