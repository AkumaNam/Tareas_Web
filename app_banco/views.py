from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Cliente
# Create your views here.

def index(request):
    return render(request, 'banco/index.html')

def cliente(request):
    return render(request, 'banco/cliente.html')