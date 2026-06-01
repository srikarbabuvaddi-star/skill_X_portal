from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm, CommentForm

@login_required
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = []
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments.append({'author': request.user.username, 'text': form.cleaned_data['text']})
            form = CommentForm()
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'form': form})
