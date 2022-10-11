from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.doctors, name='doctors'),
    path('contacts/', views.contacts, name='contacts'),
    path('profile/', views.profile, name='profile'),
    path('services/', views.services, name='services'),
    path('logIn/', views.logIn, name='logIn'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'), 
]
