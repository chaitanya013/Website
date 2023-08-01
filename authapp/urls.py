from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
]