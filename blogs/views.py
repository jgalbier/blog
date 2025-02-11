from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm

def home(request):
    """Simple rendering of home page."""
    return render(request, 'blogs/home.html')

@login_required
def check_user_is_owner(request, blog):
    if request.user != blog.owner:
        raise Http404


def blogs(request):
    """Shows the list of blogs; different if logged in."""
    all_blogs = Blog.objects.order_by('-date_added')
    try:
        my_blogs = Blog.objects.filter(owner=request.user).order_by('-date_added')
        other_blogs = []
        for blog in all_blogs:
            if blog not in my_blogs:
                other_blogs.append(blog)
        logged_in = True
        context = {'my_blogs' : my_blogs, 'other_blogs' : other_blogs, 'logged_in' : logged_in}
    except TypeError:
        logged_in = False
        context = {'all_blogs' : all_blogs, 'logged_in' : logged_in}
    return render(request, 'blogs/blogs.html', context)

@login_required
def new_blog(request):
    """View for the user to create a new blog."""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            form.save()
            return redirect('blogs:blogs')
    
    context = { 'form' : form }
    return render(request, 'blogs/new_blog.html', context)


def blog_post(request, blog_id):
    """Shows a list of posts for a given blog."""
    blog = Blog.objects.get(id=blog_id)
    
    if request.user == blog.owner:
        is_owner = True
    else:
        is_owner = False

    posts = blog.blogpost_set.order_by('-date_added')
    context = {
        'blog' : blog,
        'posts' : posts,
        'is_owner' : is_owner,
    }
    return render(request, 'blogs/blog_post.html', context)

@login_required
def new_post(request, blog_id):
    """Allows a user to create a new post for a blog they own."""
    blog = Blog.objects.get(id=blog_id)
    check_user_is_owner(request, blog)

    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
            return redirect('blogs:blog_post', blog_id=blog_id)
    
    context = {'form' : form, 'blog' : blog}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, blog_id, post_id):
    """Allows a user to edit an existing post for a blog they own."""
    blog = Blog.objects.get(id=blog_id)
    post = BlogPost.objects.get(id=post_id)
    check_user_is_owner(request, blog)

    if request.method != 'POST':
        # Different vs. new -> pass in current data since editing
        # something that already exists.
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blog_post", blog_id=blog_id)
    context = {'form' : form, 'blog' : blog, 'post' : post}
    return render(request, "blogs/edit_post.html", context)

@login_required
def delete_post(request, blog_id, post_id):
    """View to delete a blog post."""
    blog = Blog.objects.get(id=blog_id)
    check_user_is_owner(request, blog)
    post = BlogPost.objects.get(id=post_id)
    
    post.delete()
    return redirect("blogs:blog_post", blog_id=blog_id)
