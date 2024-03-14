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
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def register_user(request):
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