from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profile_list, name='profiles'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register_user, name="register"),
    path('update', views.update_user, name="update"),
    path('likes/<int:pk>', views.likes, name='likes'),
]