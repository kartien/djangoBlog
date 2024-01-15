from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('write/', views.write, name="write"),
    path('post_detail/<int:post_id>/', views.write_detail, name='detail'),
    path('posts_list/', views.post_list, name="posts_list"),

]