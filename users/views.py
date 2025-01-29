from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .forms import LoginForm
from users.models import UserRoles

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['user_login']
            password = form.cleaned_data['password']
            print(f"Authenticating: {user_login}, {password}")  # Лог для проверки

            user = authenticate(username=user_login, password=password)
            if User:
                login(request, user)
                print("Login successful!")  # Лог для проверки
                return redirect('home')
            else:
                print("Invalid credentials")  # Лог для проверки
                form.add_error(None, "Неправильний логін або пароль")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def home_view(request):
    if request.user.is_authenticated:
        user_role = request.user.user_role.user_role_name
    else:
        return login_view(request)

    return render(request, 'home.html', {'user_role': user_role})