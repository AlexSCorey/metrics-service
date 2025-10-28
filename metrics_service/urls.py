"""
URL configuration for metrics_service project.
"""

from ansible_base.lib.dynamic_config.dynamic_urls import (
    root_urls,
)
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    # Login and logout pages (with CSRF protection)
    path("health/", include("apps.health.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
    # Admin interface
    path("admin/", admin.site.urls),
    # Dashboard interface
    path("dashboard/", include("apps.dashboard.urls")),
    # API endpoints
    path("api/", include("apps.api.urls")),
    path("", include(root_urls)),
]
