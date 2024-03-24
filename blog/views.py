from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def render_post(request):
    posts = Post.objects.all()
    return render(request, "post.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def post_update(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:posts')
    return render(request, 'post_delete.html', {'post': post})
