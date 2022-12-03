from django.urls import path
from . import views

urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]