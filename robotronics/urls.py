from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('project/', views.project, name='project'),
    path('project/<int:project_id>/', views.proj, name='proj'),
    path('tutorial/<int:tutorial_id>/', views.tut, name='tut'),
]
