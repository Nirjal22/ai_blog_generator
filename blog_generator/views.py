from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

def generate_blog(request):
    pass

def login_view(request):
    if request.method == 'POST':
        usernameInput = request.POST['username']
        passwordInput = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=usernameInput, password=passwordInput)
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('/')  # Redirect to the home page
        else:
            # Handle invalid credentials
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        # Match the 'name' attributes from the HTML form
        usernameInput = request.POST['username']  # Use the corrected field name
        passwordInput = request.POST['password']

        # Check if both fields are filled
        if usernameInput and passwordInput:
            try:
                # Create the user
                user = User.objects.create_user(username=usernameInput, password=passwordInput)
                user.save()
                # Log the user in and redirect to the signout page
                login(request, user)
                return redirect('/')  # Ensure 'signout' is defined in urls.py
            except Exception as e:
                # Capture and display any errors during user creation
                error_message = f"Error creating the account: {str(e)}"
                return render(request, 'register.html', {'error_message': error_message})
        else:
            # If fields are missing, return an error message
            error_message = 'Enter valid input'
            return render(request, 'register.html', {'error_message': error_message})

    # Render the registration form if the request is GET
    return render(request, 'register.html')

def signout(request):
    logout(request)
    return redirect('/')  # Redirect to home page after logout
