from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost, Category
from .forms import BlogPostForm

def blog_list(request):
    categories = Category.objects.all()
    # Get all published posts, ordered by creation date
    posts = BlogPost.objects.filter(is_draft=False).order_by('-created_at')
    
    # Add debug message to check if posts are being found
    if not posts:
        messages.info(request, 'No published blog posts available.')
    
    return render(request, 'blog/blog_list.html', {
        'categories': categories,
        'posts': posts
    })

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = BlogPost.objects.filter(category=category, is_draft=False).order_by('-created_at')
    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts
    })

@login_required
def create_post(request):
    if not request.user.user_type == 'doctor':  # Check for doctor user type
        messages.error(request, 'Only doctors can create blog posts.')
        return redirect('blog_list')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.is_draft = form.cleaned_data.get('is_draft', False)
            post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('my_posts')
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def my_posts(request):
    if not request.user.user_type == 'doctor':  # Check for doctor user type
        messages.error(request, 'Only doctors can view their posts.')
        return redirect('blog_list')
    
    posts = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.is_draft and request.user != post.author:
        messages.error(request, 'This post is not available.')
        return redirect('blog_list')
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    # Check if the user is the author and is a doctor
    if request.user != post.author or request.user.user_type != 'doctor':
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('blog_list')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('my_posts')
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'blog/edit_post.html', {
        'form': form,
        'post': post
    }) 