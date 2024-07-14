from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            login(request, new_user)
            return redirect('dashboard.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def edit(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('dashboard.html')
    else:
        form = UserEditForm(instance=request.user.profile, data=request)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request)
    return render(request, 'edit.html', {'user_form': form, 'profile_form': profile_form})


