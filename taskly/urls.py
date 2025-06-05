from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views  # Use alias to avoid conflicts

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing page and dashboard
    path('', task_views.landing_page, name='landing_page'),
    path('dashboard/', task_views.dashboard, name='dashboard'),

    # Include all task-related routes from app
    path('tasks/', include('tasks.urls')),

    # Auth routes
    path('accounts/login/', task_views.login_view, name='login'),
    path('accounts/logout/', task_views.logout_view, name='logout'),
    path('accounts/register/', task_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Default Django auth
]
