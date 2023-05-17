from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})

