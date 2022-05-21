from django.shortcuts import render
from .models import Post
# Create your views here.


def get_all_posts(request):

    posts = Post.objects.all()

    return render(request, 'posts/home.html', {'posts': posts}) 
