from django.http import HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore
from django.contrib.auth import logout, login, authenticate # type: ignore
from django.shortcuts import render # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore

def logout_view(request):
    """Faz um Logout doo usuário."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulario em branco
        form = UserCreationForm()

    else:
        #Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(username=new_user.username, password= request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)
