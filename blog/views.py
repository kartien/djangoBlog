from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
import markdown
from .forms import PostForm, RegisterForm, LoginForm
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
    if request.method == 'POST':
        # Si el formulario fue enviado, procesar los datos
        form = LoginForm(request.POST)
        if form.is_valid():
            # Aquí puedes realizar acciones adicionales con los datos del formulario si es necesario
            # ...
            return render(request, 'auth/success.html')  # Por ejemplo, redirigir a una página de éxito
    else:
        # Si es un GET, simplemente mostrar el formulario vacío
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})