# Generated by Django 4.2.1 on 2023-06-24 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0009_loan_loan_number'),
        ('loanValues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanvalue',
            name='id',
        ),
        migrations.RemoveField(
            model_name='loanvalue',
            name='loan_id',
        ),
        migrations.AddField(
            model_name='loanvalue',
            name='loan_number',
            field=models.ForeignKey(db_column='loan_number', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_loan_number', to='loans.loan'),
        ),
        migrations.AddField(
            model_name='loanvalue',
            name='payment_ID',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
