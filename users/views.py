from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from users.forms import ProfileCreationForm
from users.models import UserProfile

# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['city'] = UserProfile.objects.get(user=request.user).city
    return render(request, 'profile.html', context)

class RegisterView(FormView):  
  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
  
  
class CreateUserProfile(FormView):  
    form_class = ProfileCreationForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('users:profile')

    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('users:login'))  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)