from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import create_account

urlpatterns = [
    path('criar-conta/', create_account, name='register'),
    path('entrar/', LoginView.as_view(), name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),
]
