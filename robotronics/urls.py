from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contacts/', views.contacts, name='contacts'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('project/', views.project, name='project'),
]
