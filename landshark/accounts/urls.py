from django.urls import path

from . import views

urlpatterns = [
    path('login',views.index, name='login'),
    path('register', views.listing, name='register'),
    path('logout', views.search, name='logout'),
    path('logout', views.search, name='dashboard')
]