# Generated by Django 3.1.6 on 2021-08-25 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0003_pet_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
