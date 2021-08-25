from django.contrib import admin
from .models import Pet, Breed, PetView, City

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(PetView)
class PetViewAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass