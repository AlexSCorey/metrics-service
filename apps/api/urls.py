"""
Main API URL configuration for metrics_service.
"""

from ansible_base.lib.dynamic_config.dynamic_urls import api_version_urls
from ansible_base.resource_registry.urls import (
    urlpatterns as resource_api_urls,
)
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "api"

urlpatterns = [
    # API version 1 (default)
    path("v1/", include("apps.api.v1.urls", namespace="v1")),
    # Django-Ansible-Base URLs (order matters - most specific first)
    path("v1/", include(resource_api_urls)),  # More specific DAB resources
    path("v1/", include(api_version_urls)),  # General DAB v1 endpoints
    # OpenAPI schema and documentation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
