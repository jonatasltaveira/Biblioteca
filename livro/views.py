from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuario.models import Usuario

# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        return HttpResponse(f'Olá {usuario}. <br>Tela de Home. Em construção...')
    else:
        return redirect('/auth/login/?status=2')
