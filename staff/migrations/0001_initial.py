# Generated by Django 4.2.1 on 2023-06-03 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staffmember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('dateofbirth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('branch', models.CharField(choices=[('Polonnaruwa', 'Polonnaruwa'), ('Hingurakgoda', 'Hingurakgoda'), ('Diyasenpura', 'Diyasenpura'), ('Sewanapitiya', 'Sewanapitiya'), ('Dehiaththakandiya', 'Dehiaththakandiya'), ('Mahiyanganaya', 'Mahiyanganaya')], default='Sewanapitiya', max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('nic', models.CharField(max_length=12)),
            ],
        ),
    ]
