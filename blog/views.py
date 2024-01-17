from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
import markdown
from .forms import PostForm
from .models import Post
# Create your views here.
def home(request):
    return render(request, 'index.html')


def info(request):
    return render(request, 'info.html')

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "post/post.html", {'form': form})


def write_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(pk=post_id)
    post.content = markdown.markdown(post.content)
    return render(request, 'post_detail.html', {'post': post})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def login(request):
    return render(request, 'auth/login.html', )

def register(request):
    pass