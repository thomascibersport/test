from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from . import forms


def login_view(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
        else:
            return redirect('/login')

    if request.user.is_authenticated:
        return redirect('/')

    return  render(request, 'login/login.html')




def register(request:HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = forms.RegisterForm()
        context = {'form': form}

        return render(request,'login/register.html', context)

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        context = {'form': form}
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('/')

        return render(request, 'login/register.html', context)

    if request.user.is_authenticated:
        return redirect('/')

def logout_view(request:HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/')