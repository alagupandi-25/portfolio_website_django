from django.urls import reverse
from django.contrib.auth import logout


class LogoutOnNonAdminPagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = request.path

        if not current_url.startswith(reverse('admin:index')) and request.user.is_authenticated:
            logout(request)

        response = self.get_response(request)
        return response
