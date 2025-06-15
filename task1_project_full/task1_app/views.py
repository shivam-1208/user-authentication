from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm
from .models import CustomUser

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Make sure 'login' is named in urls.py
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Use the correct view name from urls.py
        else:
            context['error'] = 'Incorrect username or password.'

    return render(request, 'login.html', context)  # Always return a response


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def all_users_view(request):
    users = CustomUser.objects.all()
    return render(request, 'all_users.html', {'users': users})
