from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_projects, name='projects'),
    path('create/', views.post_project, name='post_project'),
    path('<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('<int:pk>/view_project/', views.view_project, name='view_project'),
]