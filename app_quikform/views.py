from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from app_quikform.models import User, Pergunta, Formulario, Resposta, Contato, Newsletter
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
            user.token_confirmation = User.generate_token_confirmation(32)
            user.token_expiration_date = User.generate_token_expiration_date(15)
            user.save()
            user.send_email_confirm_register(request)
            return redirect('/cadastro')
    return render(request, "user/cadastro.html")

def confirmar_email(request, user_id, token):
    try:
        user = User.objects.filter(id=user_id).first()
        print(user.token_confirmation)
        print(token)
        #if token != user.token_confirmacao:
        #    return HttpResponse('Token de confirmação inválido.')
        user.is_confirmed = True
        user.save()

        return redirect('/login')
    except user.DoesNotExist:
        return HttpResponse('Usuário não encontrado.')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user_validation = User.objects.get(username=username)
        if user_validation.check_password(password):
            if not user_validation.is_confirmed:
                messages.error(request, "Desculpe, mas você ainda não confirmou seu cadastro")
                return redirect('/login')
        else:
            messages.error(request, "Seu usuário ou senha estão incorretos.")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Seu usuário ou senha estão incorretos.")
    return render(request,'user/login.html')

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
    return render(request, 'user/redefinir_email.html')

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
    return render(request, 'user/redefinir_senha.html', {'token':token})

@login_required(login_url='/login/')
def inicial(request):
    user = User.objects.get(username=request.user)
    return render(request, 'inicial.html', {'user': user})

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def gerenciador_formulario(request):
    username = request.user
    user = User.objects.get(username=username)
    formularios = Formulario.objects.filter(user_id_id=user.id)

    return render(request,'form/gerenciador_form.html',{'formularios':formularios})
@login_required(login_url='/login/')
def formulario(request,formulario_id):
    perguntas = Pergunta.objects.filter(formulario_id_id=formulario_id)
    formulario = Formulario.objects.get(id=formulario_id)
    return render(request,'form/formulario.html',{'perguntas':perguntas,'formulario':formulario})

def delete_formulario(request, formulario_id):
    formulario = Formulario.objects.get(id=formulario_id)
    formulario.delete()
    return redirect('/gerenciador_formulario')

@login_required(login_url='/login/')
def add_pergunta(request):
    if request.method == 'POST':
        formulario_id = request.POST.get('formulario_id')
        descricao = request.POST.get('inputPergunta')
        
        pergunta = Pergunta(descricao=descricao,formulario_id_id=formulario_id)
        pergunta.save()

        resposta = Resposta(pergunta_id_id=pergunta.id)
        resposta.save()

        formulario = Formulario.objects.get(id=formulario_id)
        formulario.addPergunta()
        formulario.save()
    return redirect(f'/formulario/{formulario_id}')

@login_required(login_url='/login/')
def delete_pergunta(request,id_pergunta):
    pergunta = Pergunta.objects.get(id=id_pergunta)
    formulario_id = pergunta.formulario_id_id
    pergunta.delete()
    formulario = Formulario.objects.get(id=formulario_id)
    formulario.deletePergunta()
    formulario.save()
    return redirect(f'/formulario/{formulario_id}')

@login_required(login_url='/login/')
def add_formulario(request):
    username = request.user
    user = User.objects.get(username=username)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')

        formulario = Formulario(titulo=titulo, categoria=categoria, user_id_id=user.id)
        formulario.save()
    return redirect('/gerenciador_formulario')

@login_required(login_url='/login/')
def resposta_formulario(request, formulario_id):
    formulario = Formulario.objects.get(id=formulario_id)
    perguntas = Pergunta.objects.filter(formulario_id_id=formulario_id)
    userId = User.objects.get(username=request.user).id
    respostas = Resposta.objects.all()

    if request.method == "POST":
        id_resposta = int(request.POST.get('id_resposta'))
        resposta = request.POST.get('resposta')

        respostaDal = Resposta.objects.get(id=id_resposta)
        respostaDal.resposta = resposta
        respostaDal.user_id_id = userId
        respostaDal.save()

        formulario.addResposta()
        formulario.save()
    return render(request, "form/form_visivel.html", {"perguntas":perguntas, "formulario":formulario, "respostas":respostas})

@login_required(login_url='/login/')
def contato(request):
    userId = User.objects.get(username=request.user).id

    if request.method == 'POST':
        email = request.POST.get('email')
        comentario = request.POST.get('comentario')

        contato = Contato(email=email, comentario=comentario, user_id_id=userId)
        contato.save()
        return redirect('/')

@login_required(login_url='/login/')
def newsletter(request):
    userId = User.objects.get(username=request.user).id
    if request.method == 'POST':
        email = request.POST.get('email')

        newsletter = Newsletter(email=email, user_id_id=userId)
        newsletter.save()
        return redirect('/')
    
