from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'account/login.html')


def register(request):
    return render(request, 'account/register.html')


def forgot_password(request):
    return render(request, 'account/forgot-password.html')
