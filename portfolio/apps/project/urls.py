from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('read/', views.read_projects, name='read_projects'),
    path('create/', views.create_project, name='create_project'),
    path('<int:pk>/update/', views.update_project, name='update_project'),
    path('<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('<int:pk>/view/', views.view_project, name='view_project'),
]