from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('read/', views.tools, name='tools'),
    path('create/', views.create_tool, name='create_tool'),
    path('<int:pk>/delete/', views.delete_tool, name='delete_tool'),
    path('<int:tool_id>/move/', views.move_tool, name='move_tool'),
]