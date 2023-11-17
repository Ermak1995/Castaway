from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm


def index(request):
    return render(request, 'index.html')

def page_404(request):
    return HttpResponse('404')

def register(request):
    '''
    ['add_error', 'add_initial_prefix', 'add_prefix', 'as_div', 'as_p', 'as_table', 'as_ul', 'auto_id', 'base_fields', 'changed_data', 'clean', 'clean_password2', 'clean_username', 'data', 'declared_fields', 'default_renderer', 'empty_permitted', 'error_class', 'error_messages', 'errors', 'field_order', 'fields', 'files', 'full_clean', 'get_context', 'get_initial_for_field', 'has_changed', 'has_error', 'hidden_fields', 'initial', 'instance', 'is_bound', 'is_multipart', 'is_valid', 'label_suffix', 'media', 'non_field_errors', 'order_fields', 'prefix', 'render', 'renderer', 'save', 'template_name', 'template_name_div', 'template_name_label', 'template_name_p', 'template_name_table', 'template_name_ul', 'use_required_attribute', 'validate_unique', 'visible_fields']

    '''
    # error = ''
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # and User.objects.filter(email=email).exists()
            form.save()
            return redirect('index')
        else:
            print(dict(form.errors))
            errors = form.errors
    else:
        form = UserRegisterForm()
        # print(dir(form))
        # print([field.name for field in form])
    context = {
        'form': form,

    }
    return render(request, 'registration.html', context=context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return page_404(request)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
