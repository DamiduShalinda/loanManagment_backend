# Generated by Django 4.2.1 on 2023-07-14 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('StaffProfile', '0001_initial'),
        ('loans', '0002_alter_loan_first_guarantor_and_more'),
        ('loanvalues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loanarrears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_payment', models.FloatField()),
                ('monthly_arrears', models.FloatField()),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loanarrears', to='loans.loan')),
                ('loan_values', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loanarrears', to='loanvalues.loanvalue')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loanarrears', to='StaffProfile.staffprofile')),
            ],
        ),
    ]