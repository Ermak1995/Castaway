from django.shortcuts import render
from .forms import UserRegisterForm

def index(request):
    return render(request, 'index.html')


def register(request):
    form = UserRegisterForm()
    return render(request, 'registration.html', {'form': form})