from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.urls import reverse
import os
from dotenv import load_dotenv
load_dotenv()


class User(AbstractUser):
    token_confirmation = models.CharField(max_length=100, null=True, blank=True)
    token_expiration_date = models.DateTimeField(null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)

    def generate_token_confirmation(length):
        return get_random_string(length=length)
    
    def generate_token_expiration_date(minutes):
        return timezone.now() + timezone.timedelta(minutes=minutes)
    
    def send_email_confirm_register(self, request):
        subject = "Confirme seu email"
        message = f'Clique no link a seguir para confirmar seu email: {request.build_absolute_uri(reverse("confirmar_email", args=[self.id, self.token_confirmation]))}'
        from_email = os.getenv('EMAIL_HOST_USER')
        recipient_list = [self.email]
        send_mail(subject, message, from_email, recipient_list)

    def send_email_redefinicao_senha(request, token, email):
        subject = "Redefinir senha"
        message = f'Clique no link a seguir para redefinir sua senha: {request.build_absolute_uri(reverse("redefinir_senha", args=[token]))}'
        from_email = os.getenv('EMAIL_HOST_USER')
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

class Formulario(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=255, null=False)
    categoria = models.TextField(max_length=255, null=False)
    numero_pergunta = models.IntegerField(null=False, default=0)
    numero_resposta = models.IntegerField(null=False, default=0)
    data_criacao = models.DateField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=False)

    def addPergunta(self):
        self.numero_pergunta += 1

    def deletePergunta(self):
        self.numero_pergunta -= 1

    def addResposta(self):
        self.numero_resposta =+ 1

    
class Pergunta(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=255, null=False)
    formulario_id = models.ForeignKey(Formulario, on_delete=models.CASCADE,null=True)

class Resposta(models.Model):
    id = models.AutoField(primary_key=True)
    resposta = models.TextField(max_length=255, null=True, default="")
    pergunta_id = models.ForeignKey(Pergunta, on_delete=models.CASCADE,null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField(max_length=100, null=False)
    comentario = models.TextField(max_length=255, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField(max_length=100, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

