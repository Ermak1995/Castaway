from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegisterForm, LoginForm
from .models import Episodes, Tags



def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    episodes = Episodes.objects.order_by('-time_create')[:3]
    return render(request, 'index.html', {'episodes': episodes, 'num_visits':num_visits})


def page_404(request):
    return HttpResponse('404')


def register(request):
    '''
    ['add_error', 'add_initial_prefix', 'add_prefix', 'as_div', 'as_p', 'as_table', 'as_ul', 'auto_id', 'base_fields', 'changed_data', 'clean', 'clean_password2', 'clean_username', 'data', 'declared_fields', 'default_renderer', 'empty_permitted', 'error_class', 'error_messages', 'errors', 'field_order', 'fields', 'files', 'full_clean', 'get_context', 'get_initial_for_field', 'has_changed', 'has_error', 'hidden_fields', 'initial', 'instance', 'is_bound', 'is_multipart', 'is_valid', 'label_suffix', 'media', 'non_field_errors', 'order_fields', 'prefix', 'render', 'renderer', 'save', 'template_name', 'template_name_div', 'template_name_label', 'template_name_p', 'template_name_table', 'template_name_ul', 'use_required_attribute', 'validate_unique', 'visible_fields']
    '''
    # error = ''
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
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
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login details')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def show_episodes(request):
    episodes = Episodes.objects.all()
    tags = Tags.objects.all()
    return render(request, 'episodes.html', {'episodes': episodes, 'tags': tags})


def episodes_detail(request, episode_id):
    ep = get_object_or_404(Episodes, pk=episode_id)
    return render(request, 'episodes_detail.html', {'ep': ep})


def show_all_tags(request):
    tags = Tags.objects.all()
    return render(request, 'all_tags.html', {'tags': tags})


def show_tags(request, tag_slug):
    tag = Tags.objects.get(slug=tag_slug)
    episodes = Episodes.objects.filter(tags__in=[tag])
    return render(request, 'tags.html', {'episodes': episodes, 'tag': tag})
