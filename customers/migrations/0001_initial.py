# Generated by Django 4.2.1 on 2023-07-03 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('surname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('telephone1', models.CharField(max_length=100)),
                ('telephone2', models.CharField(max_length=100)),
                ('dateofbirth', models.DateTimeField(null=True)),
                ('nicnumber', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
        ),
    ]
