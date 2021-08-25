from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Breed(models.Model):
    breed_name = models.CharField(max_length=100)

    def __str__(self):
        return self.breed_name

class PetView(models.Model):
    pet_view = models.CharField(max_length=50)

    def __str__(self):
        return self.pet_view

class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Pet(models.Model):
    name = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    date = models.DateField()
    pet_view = models.ForeignKey(PetView, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/')
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)
    users = models.ManyToManyField(User, related_name='favorite_posts', blank=True, null=True)

    def __str__(self):
        return self.name