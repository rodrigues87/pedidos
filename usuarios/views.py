from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect


def base(request):
    return render(request, 'site/base.html')


def login_user(request):
    return render(request, 'site/login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário e senha inválido. Favor tentar novamente.")
    return redirect('/home/')


def administrador(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/pedidos/solicitar')


@login_required
def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return redirect('/login/')
    else:
        messages.error(request, "Usuário não está logado")
        return redirect('/login/')
