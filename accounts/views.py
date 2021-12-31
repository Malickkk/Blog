from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate


from .forms import CustomUserCreationForm, LoginForm
from .decorators import unauthenticated_user


def signup(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{form.cleaned_data["username"]} registered successfully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'signup.html', context)


@unauthenticated_user
def login(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user is not None:
                login(request, user)
                messages.info('Hey! {user.username}! You have been logged in')
            else:
                messages.info('Incorrect credentials. Login failed!')
    context = {'form': form, 'message': message}
    return render(request, 'login.html', context)


def logout(request):
    logout(request)
    return redirect('index')

# Create your views here.
