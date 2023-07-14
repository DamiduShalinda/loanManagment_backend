# Generated by Django 4.2.1 on 2023-07-12 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loans', '0002_alter_loan_first_guarantor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='loanValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('payment_amount', models.FloatField()),
                ('interest', models.FloatField(null=True)),
                ('principle', models.FloatField(null=True)),
                ('balance', models.FloatField(null=True)),
                ('loan_number', models.ForeignKey(db_column='loan_number', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_loan_number', to='loans.loan')),
            ],
        ),
    ]