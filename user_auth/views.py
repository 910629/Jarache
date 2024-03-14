from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_login(request):
    """This function is used in a login view of the application.
    It renders the 'registration/login.html' template, which 
    contains a login form for users to authenticate.

    :param request: An HTTP request object.

    :Returns: An HTTP response object with the rendered login form template.
    """
    return render(request, 'registration/login.html')


def authenticate_user(request):
    """This method processes user authentication based on submitted credentials.
    It handles user login requests by retrieving username and password
    from the POST data (`request.POST`). It attempts to authenticate the user
    using Django's `authenticate` function.
    - If authentication fails (user is None), the function redirects the user
      back to the login page (`reverse('user_auth:login')`).
    - On successful authentication, the user is logged in using `login(request, user)`
      and redirected to the 'user_auth:show_user' URL (a profile page).

    :param request: An Http request object.

    :returns:   HttpresponseRedirect: redirects user to login page if authentication fails
                HttpresponseRedirect: redirects user to user profile page if authentication is successful
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
            )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user'))
    

@login_required(login_url='user_auth:login')
def show_user(request):
    """This function displays user profile information (password is hashed by Django for security reasons).
    It retrieves the currently authenticated user's information
    from the request object (`request.user`). It's decorated with
    `@login_required` to ensure only authenticated users can access this view.

    
    :param request: An HTTP request object.

    :returns:   An HTTP response object with the rendered 'authentication/user.html' template
                containing the user's profile information (password hashed).
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def register_user(request):
    """This function handles user registration requests and creates new user accounts.
    It checks if the request method is POST, then:

        - Creates a `UserCreationForm` instance using the submitted data (`request.POST`).
        - Validates the form data using `form.is_valid()`.
        - If valid:
            - Saves the new user using `form.save()`.
            - Logs the user in using `login(request, user)`.
            - Redirects the user to the profile page (`reverse('user_auth:show_user')`).
        - If invalid:
            - Creates an empty `UserCreationForm` instance for the user to correct errors.
    
    Or else:
        - Creates an empty `UserCreationForm` instance for the registration form.

    The function then renders the 'authentication/registration.html' template,
    passing the appropriate form object (`form`) for display and form completion.

    :param request: An HTTP request object.

    :Returns:   An HTTP response object:
            - Renders the registration form template (GET request).
            - Renders the registration form template with validation errors (POST request, invalid form).
            - Redirects to the user profile page on successful registration (POST request, valid form).
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:show_user')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/registration.html', {'form': form})
        

def logout_view(request):
    logout(request)
    return redirect('poll:poll')