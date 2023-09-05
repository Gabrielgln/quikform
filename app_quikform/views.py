from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        email = request.POST.get('email')
        first_name = request.POST.get('nome')
        password = request.POST.get('password')

        result = User.objects.filter(username=username).first()
        if result:
            messages.error(request, "Este nome de usuário já está em uso. Tente outro.")
        else:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            first_name=first_name,
                                            password=password)
            user.save()
            login(request, user)
            redirect('/')
    return render(request, "cadastro.html")

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('/')
        else:
            messages.error(request, "Seu usuário ou senha estão incorretos.")
    return render(request,'login.html')