from django.shortcuts import redirect
from django.urls import reverse

class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == reverse('login'):
            return redirect(reverse('dashboard'))  # Ensure this uses reverse to get the correct absolute URL
        response = self.get_response(request)
        return response
