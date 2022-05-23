from turtle import pos
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CreatePostForm, UpdatePostForm
from django.contrib import messages
# Create your views here.


def get_all_posts(request):

    posts = Post.objects.all()

    return render(request, 'posts/home.html', {'posts': posts}) 



def create_post(request):
    context = {}
    form = CreatePostForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            creator = request.user
            new_post = form.save(commit=False)
            new_post.creator = creator
            new_post.save()
            return redirect('posts')
    
    context.update({
        'form': form,
    })

    return render(request, 'posts/create_post.html', context=context)


def update_post(request, p_id):
    post = Post.objects.get(id=p_id)

    if request.method == 'POST':
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    
    else:
        form = UpdatePostForm(instance=post)
    context = {
        'form': form,
    }

    return render(request, 'posts/update_post.html', context=context)

    
def delete_post(request, p_id):
    post = get_object_or_404(Post, pk=p_id)
    post.delete()
    messages.success(request, 'Post deleted successfully', 'info')
    return redirect('posts')