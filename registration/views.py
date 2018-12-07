from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm, RegisterForm


@login_required
def home(request):
    return render(request, 'home.html', {})


def login_view(request):
    """
    View to login.
    """
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        redirect('/home/')
    return render(request, 'login.html', context={'form': form})


def register_view(request):
    """
    View to register new users.
    """
    next = request.GET.get('next')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password=password)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=user.password)
        login(request, new_user)
        # if next:
        #     return redirect(next)
        print "REDIRECCIONA"
        redirect('/home/')
    return render(request, 'register.html', context={'form': form})


def logout_view(request):
    """
    A view to logout. 
    """
    logout(request)
    return redirect('/')

