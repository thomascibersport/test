from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


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

    return  render(request, 'login/login.html')


def register(request:HttpRequest) -> HttpResponse:
    return render(request,'login/register.html')

def logout_view(request:HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/')