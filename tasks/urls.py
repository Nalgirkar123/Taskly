from django.urls import path
from . import views

urlpatterns = [
    # Task views
    path('', views.task_list, name='task_list'),  # e.g., /tasks/
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('tasks/<int:pk>/update-status/', views.update_task_status, name='update_task_status'),

    # Optional: You can remove the register view from here since it's already handled in project urls
]
