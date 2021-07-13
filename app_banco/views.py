from functools import reduce
from django.db import reset_queries
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import admin, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Cliente
# Create your views here.

@login_required
def index(request):
    return render(request, 'banco/index.html')

@login_required
def cliente(request):

    return render(request, 'banco/cliente.html')

@login_required
def transferencias(request):
    
    return render(request, 'banco/transacciones.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')

        user = authenticate(username=username, password=password)

        
        if user is not None:
            if  username != admin:
                login(request, user)
                return redirect(reverse('index'))
            elif request.user.is_superuser():
                return redirect(reverse('cliente'))
            else:
                return HttpResponse('El usuario existe pero no esta activo')

        else:
            messages.add_message(request, messages.ERROR, ' El usuario/contraseña invalidos o la cuenta esta desactivada')
            return render(request, 'banco/login.html')
    else:
        return render(request, 'banco/login.html')

def log_out(request):
    logout(request)
    return redirect('login_view')