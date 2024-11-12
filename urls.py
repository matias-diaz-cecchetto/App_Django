from django.urls import path
from notifications import admin, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('notifications/<int:notification_id>/mark-as-read/', views.mark_as_read, name='mark_as_read'),
]
