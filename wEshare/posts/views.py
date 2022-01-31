from re import template
from django.shortcuts import render, redirect, reverse, get_object_or_404
from allauth.account.forms import LoginForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # added messages for editing success/warning
from .models import Post
from .forms import PostForm
import datetime

now = datetime.datetime.now()
display_post = False
if 9 < now.hour < 12:
    display_post = True

# Create your views here.
def index(request):
    """ A view to return the index page """
    
    template = 'index.html'
    context ={
        'LoginForm': LoginForm,
        'SignupView': SignupView,
    }
    return render(request, template, context)


@login_required
def view_posts(request):
    """ A view to return the posts page """

    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)


@login_required
def create_post(request):
    """ A view to create a new post """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect(reverse('view_posts'))
    else:
        form = PostForm()

    template = 'create_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def will_expire(self):
    """ A view to set an expiration time on posts """
    if self.date_published <= datetime.datetime.now():
            self.delete()
            return False
