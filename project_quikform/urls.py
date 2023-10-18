from django.contrib import admin
from django.urls import path
from app_quikform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.inicial, name='inicial'),
    path('redefinir_email/', views.redefinir_email, name='redefinir_email'),
    path('redefinir_senha/<str:token>/', views.redefinir_senha, name='redefinir_senha'),
    path('formulario/<int:formulario_id>', views.formulario, name='formulario'),
    path('formulario/add_pergunta/', views.add_pergunta, name='add_pergunta'),
    path('formulario/delete_pergunta/<int:id_pergunta>', views.delete_pergunta, name='delete_pergunta'),
    path('gerenciador_formulario/', views.gerenciador_formulario, name='gerenciador_formulario'),
    path('gerenciador_formulario/add_formulario/', views.add_formulario, name='add_formulario'),
]
