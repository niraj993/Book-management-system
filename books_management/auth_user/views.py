from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Register view
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken!')
                return redirect('register_user')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, f'Account created for {username}!')
                return redirect('login_user')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register_user')
    
    return render(request, 'auth/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('/')  
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login_user')
    
    return render(request, 'auth/login.html')



def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login_user')
