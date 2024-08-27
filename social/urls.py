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
    path('show/<int:pk>', views.show, name='show'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('profile/following/<int:pk>', views.following, name='following'),
    path('delete_tweet/<int:pk>', views.delete_tweet, name='delete_tweet'),
    path('edit_tweet/<int:pk>', views.edit_tweet, name='edit_tweet'),
    path('search_posts', views.search_posts, name="search_posts"),
    path('search_users', views.search_users, name="search_users"),
    path('comment/', views.comment, name='comment'),
]