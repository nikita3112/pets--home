from django.urls import path, include
from .views import main, PetsView, PetView


urlpatterns = [
    path('', main, name='main'),
    path('pets/', PetsView.as_view(), name='pets'),
    path('pets/<str:pk>/', PetView.as_view(), name='pet-detail'),
]