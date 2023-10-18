from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app_quikform.models import User, Pergunta, Formulario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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
            return redirect('/')
    return render(request, "cadastro.html")

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)
        if user is not None:
            print('entrou')
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Seu usuário ou senha estão incorretos.")
    return render(request,'login.html')

def redefinir_email(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        print(email)
        try:
            usuario = User.objects.get(email=email)
            if usuario is not None:
                usuario.token_confirmation = User.generate_token_confirmation(32)
                usuario.token_expiration_date = User.generate_token_expiration_date(15)
                usuario.save()

                User.send_email_redefinicao_senha(request, usuario.token_confirmation, usuario.email)
        except User.DoesNotExist:
            messages.error(request, 'Usuário inexistente.')
    return render(request, 'redefinir_email.html')

def redefinir_senha(request, token):
    if request.method == 'POST':
        try:
            usuario = User.objects.get(token_confirmation=token)
            if usuario is not None:
                now = timezone.now().timestamp()
                if now < usuario.token_expiration_date.timestamp():
                    password = request.POST.get('password')
                    confirm_password = request.POST.get('confirmPassword')
                    if password == confirm_password:
                        usuario.set_password(password)
                        usuario.token_confirmation = None
                        usuario.token_expiration_date = None
                        usuario.save()
                        return redirect('/')
                    else:
                        messages.error(request, "As senhas não correspondem. Tente novamente.")
                else:
                    usuario.token_confirmation = None
                    usuario.token_expiration_date = None
                    usuario.save()
                    messages.error(request, "A solicitação de redefinição de senha expirou. Tente novamente.")
        except User.DoesNotExist:
            messages.error(request, "Usuário inexistente.")
    return render(request, 'redefinir_senha.html', {'token':token})

@login_required(login_url='/login/')
def inicial(request):
    user = User.objects.get(username=request.user)
    return render(request, 'inicial.html', {'user': user})

def logout_user(request):
    logout(request)
    return redirect('/')

def formulario(request,formulario_id):
    perguntas = Pergunta.objects.filter(formulario_id_id=formulario_id)
    formulario = Formulario.objects.get(id=formulario_id)
    return render(request,'formulario.html',{'perguntas':perguntas,'formulario':formulario})


def add_pergunta(request):
    if request.method == 'POST':
        formulario_id = request.POST.get('formulario_id')
        descricao = request.POST.get('inputPergunta')
        print(formulario_id)
        
        pergunta = Pergunta(descricao=descricao,formulario_id_id=formulario_id)
        pergunta.save()


    return redirect(f'/formulario/{formulario_id}')

def delete_pergunta(request,id_pergunta):
        
    pergunta = Pergunta.objects.get(id=id_pergunta)
    formulario_id = pergunta.formulario_id_id
    pergunta.delete()

    return redirect(f'/formulario/{formulario_id}')

def gerenciador_formulario(request):
    username = request.user
    user = User.objects.get(username=username)
    formularios = Formulario.objects.filter(user_id_id=user.id)

    return render(request,'gerenciador_form.html',{'formularios':formularios})

def add_formulario(request):
    username = request.user
    user = User.objects.get(username=username)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')

        formulario = Formulario(titulo=titulo, categoria=categoria, user_id_id=user.id)

        formulario.save()

    return redirect('/gerenciador_formulario')

