from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('episodes/', views.show_episodes, name='show_episodes'),
    path('episodes/<int:episode_id>', views.episodes_detail, name='episodes_detail'),
    path('tags/', views.show_all_tags, name='show_all_tags'),
    path('tags/<int:tag_id>', views.show_tags, name='show_tags'),
]