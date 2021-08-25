from django.db import models
from django.contrib.auth.models import User
from pets.models import City

# Create your models here.
class UserProfile(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
