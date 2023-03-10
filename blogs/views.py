from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """Welcoming page for Blog"""
    return render(request, "blogs/index.html")

def home(request):
    """Home page for Blog"""
    blogposts = BlogPost.objects.order_by("date_added")
    context = {"blogposts": blogposts}

    return render(request, "blogs/home.html", context)


@login_required
def new_post(request):
    """Create new blog post for the website"""
    if request.method != 'POST':
        # No data; create a blank form
        form = BlogPostForm()
    else:
        # POST data submitted; process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect("blogs:home")
    
    # Display invalid or blank form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, blogpost_id):
    """Edit an existing blog post"""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    if blogpost.author != request.user:
        raise Http404

    if request.method != 'POST':
        # No POST data received; show an info-existing form
        form = BlogPostForm(instance=blogpost)
    
    else:
        # POST data submitted, process data to save new info
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:home")
    
    context = {'form': form, 'blogpost': blogpost}
    return render(request, "blogs/edit_post.html", context)
