from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def home_view(request):
    return render(request, 'user_auth/home.html', {'username': request.user.username})

from django.shortcuts import render, redirect

def index_view(request):
    if request.user.is_authenticated:
        return redirect('home') 
    return render(request, 'user_auth/index.html')


