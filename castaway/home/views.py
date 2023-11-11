from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration.html', {'form': form})