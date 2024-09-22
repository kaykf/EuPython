from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]