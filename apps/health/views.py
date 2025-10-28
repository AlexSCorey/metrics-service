"""Health check views for metrics service. Primarily used by aap-dev"""

from django.http import JsonResponse


def ping(request):
    return JsonResponse({"status": "ok", "message": "Service is alive"})
