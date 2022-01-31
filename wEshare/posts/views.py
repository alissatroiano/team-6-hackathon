from re import template
from django.shortcuts import render, redirect, reverse, get_object_or_404
from allauth.account.forms import LoginForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # added messages for editing success/warning

from django.views.generic import UpdateView  # meant to use this as default django method in edit_post
from django.forms.models import modelformset_factory
from .models import Post
from .forms import PostForm

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

# @login_required
# def edit_post(request, post_id):
#     """ Editing existing posts """
#     post = get_object_or_404(Post, unique_id=post_id)
#     PostFormSet = modelformset_factory(
#         Post, fields=('description', 'content'),form=PostForm, extra=0)
    
#     if request.method == 'GET':
#         formset = PostFormSet(queryset=Post.objects.filter(post=post))
#         return render(request, 'edit_posts.html', {'formset': formset})
#     else:
#         formset = PostFormSet(request.POST, queryset=Post.objects.filter(post=post))
#         if formset.is_valid():
#             formset.save()
#             return redirect('view_posts')
#         else:
#             return render(request, template, context)
 