from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tools, name='tools'),
    path('add/', views.post_tool, name='post_tool'),
    path('<int:pk>/delete/', views.delete_tool, name='delete_tool'),
    path('<int:tool_id>/move/', views.move_tool, name='move_tool'),
]
