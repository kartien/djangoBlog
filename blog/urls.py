from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name="info"),
    path('write/', views.write, name="write"),
    path('post_detail/<int:post_id>/', views.write_detail, name='detail'),
    path('posts_list/', views.post_list, name="posts_list"),
    # authentication
    path('login/', views.login, name="login"),
    path('register/', views.register, name='register/'),
]