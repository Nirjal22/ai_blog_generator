from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signout(request):
    return render(request, 'signout.html')

def register(request):
    if request.method == 'POST':
        usernameInput = request.POST.get('username')
        passwordInput = request.POST.get('password')

        if usernameInput and passwordInput:
            try:
                user = User.objects.create_user(username=usernameInput, password=passwordInput)
                user.save()
                login(request, user)  # Pass the request object and the user object
                return redirect('signout')
            except:
                error_message = "Error creating the account"
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Enter valid input'
            return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')