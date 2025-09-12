"""
URL configuration for metrics_service project.
"""

from ansible_base.lib.dynamic_config.dynamic_urls import (
    api_version_urls,
    root_urls,
)
from ansible_base.resource_registry.urls import (
    urlpatterns as resource_api_urls,
)
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.api.v1.views import ping

urlpatterns = [
    # Login and logout pages (with CSRF protection)
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
    # Admin interface
    path("admin/", admin.site.urls),
    # Dashboard interface
    path("dashboard/", include("apps.dashboard.urls")),
    # OpenAPI schema and documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Django-Ansible-Base URLs
    path("api/v1/", include(api_version_urls)),
    path("api/v1/", include(resource_api_urls)),
    # API endpoints
    path("api/", include("apps.api.urls")),
    path("ping/", ping, name="ping"),
    path("", include(root_urls)),
]
