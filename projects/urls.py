from django.urls import path
from . import views
from projects import views as contact_views

urlpatterns = [
    path('', views.home, name="home"), # this is the home page
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"), 
    path('contact/', views.contact, name="contact"),
]