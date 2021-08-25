from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Pet
from users.models import UserProfile

# Create your views here.
def main(request):
    data = Pet.objects.all()

    return render(request, 'main.html', {"data": data})

class PetsView(ListView):
    model = Pet
    template_name = 'pets_template.html'
    context_object_name = 'pets'

class PetView(DetailView):
    model = Pet
    template_name = "pet_detail.html"
    context_object_name = "pet"