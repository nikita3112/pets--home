# Generated by Django 3.1.6 on 2021-08-24 10:48

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
