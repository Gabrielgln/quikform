from django.contrib import admin
from django.urls import path
from app_quikform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('inicial/', views.inicial, name='inicial')
]
