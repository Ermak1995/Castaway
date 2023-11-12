from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data()
            form.save(**data)
            redirect('index')
    else:
        form = UserRegisterForm()
        print(form)
    return render(request, 'registration.html', {'form': form})