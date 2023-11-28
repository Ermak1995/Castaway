from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('episodes/', views.show_episodes, name='show_episodes'),
]