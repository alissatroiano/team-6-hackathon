from django.shortcuts import render

from allauth.account.forms import LoginForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required

from .models import Post

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
    # posts = Post.objects.all()
    return render(request, 'posts.html')
