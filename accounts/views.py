from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm
from django.core.mail import send_mail
from django.conf import settings
from .models import MagicLinkToken
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/registo.html', {'form': form})

def magic_link_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            token = MagicLinkToken.objects.create(user=user)
            link = request.build_absolute_uri(f'/accounts/magic-link/{token.token}/')
            send_mail(
                'O teu link de acesso',
                f'Clica aqui para entrar: {link}',
                settings.EMAIL_HOST_USER,
                [email],
            )
            return render(request, 'accounts/magic_link_enviado.html')
        except User.DoesNotExist:
            return render(request, 'accounts/magic_link_request.html', {'erro': 'Email não encontrado'})
    return render(request, 'accounts/magic_link_request.html')

def magic_link_verify(request, token):
    try:
        magic_token = MagicLinkToken.objects.get(token=token, usado=False)
        login(request, magic_token.user)
        magic_token.usado = True
        magic_token.save()
        return redirect('index')
    except MagicLinkToken.DoesNotExist:
        return render(request, 'accounts/magic_link_invalido.html')