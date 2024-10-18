from django.shortcuts import render
from .models import Post
# Create your views here.
posts = Post.objects.all()
context = {
    'posts': posts
}

def home(req):
    return render(req, 'blog/home.html', context)