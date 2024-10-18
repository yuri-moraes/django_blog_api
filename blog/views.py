from django.shortcuts import render
from .models import Post
# Create your views here.
def home(req):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(req, 'blog/home.html', context) 

def get_post_detail(req, post_id):
    post = Post.objects.get(pk=post_id)
    context = { 'post': post }
    return render(req, 'blog/post_detail.html',context)