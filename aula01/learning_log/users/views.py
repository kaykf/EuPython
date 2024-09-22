from django.http import HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore
from django.contrib.auth import logout # type: ignore

def logout_view(request):
    """Faz um Logout doo usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))