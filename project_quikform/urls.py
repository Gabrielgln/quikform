from django.contrib import admin
from django.urls import path
from app_quikform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('', views.inicial, name='inicial'),
    path('redefinir_email/', views.redefinir_email, name='redefinir_email'),
    path('redefinir_senha/', views.redefinir_senha, name='redefinir_senha')
]
