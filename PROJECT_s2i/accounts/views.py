from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birthday = form.cleaned_data.get('birthday')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')

    else:
        logout(request)
        form = RegistrationForm()
    
    return render(request, 'accounts/signup.html', {'form':form})