from django.urls import path, include, reverse_lazy
from users.views import RegisterView, CreateUserProfile, index
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('profile/', index, name='profile'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='register.html', success_url=reverse_lazy('users:profile-create')), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]