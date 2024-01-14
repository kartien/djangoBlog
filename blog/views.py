from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def write(request):
    return render(request, "post/post.html")