from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import *

from django.contrib.auth import authenticate, login, logout as dlogout


def ajaxsignup(request):
    ajax = AjaxSignUp(request.POST)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxlogin(request):
    ajax = AjaxLogin(request.POST)
    logged_in_user, output = ajax.validate()
    if logged_in_user is not None:
        login(request, logged_in_user)
    context = {'ajax_output': output}
    return render(request, 'ajax.html', context)


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def gallery(request):
    return render(request, 'gallery.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    context = {}
    return render(request, 'register.html', context)
