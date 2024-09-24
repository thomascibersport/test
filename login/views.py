from django.contrib.auth import authenticate, login, logout, forms
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
    if request.method == "GET":
        form = forms.RegisterForm()
        context = {'form': form}

        return render(request,'login/register.html', context)

def logout_view(request:HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/')