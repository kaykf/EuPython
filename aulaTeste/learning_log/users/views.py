from django.shortcuts import render # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore
from .forms import LoginForm
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth import login as authLogin # type: ignore

def login(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username= username, password=password)

            if user:
                authLogin(request, user)
                return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'user/login.html', context)
