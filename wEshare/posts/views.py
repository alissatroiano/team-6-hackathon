from django.shortcuts import render, redirect, reverse
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

    return render(request, template, context)

    # Dear Alissa, each video I watched that was uploaded within last year or less
    # Has had a new html file with the edit/update post which this function would
    # Redirect them, but we dont do it like that, I might be missing some logic behind
    # the functions that you created and fair play for making those, but, after trying 
    # this function still doesn't work, I would really have preffered that i figured
    # it out but somehow I dont, I will wake up much before submission so maybe we
    # could chat if I could be of any help, but I put this in comment since it would
    # not open the page for me to test it, so this is why i will comment out anything
    # related to 'edit_post' func, hope that any of this code helps but if not, feel
    # free to arrange your own since the consistency is also relevant, its 7:40 so I
    # will leave it in hope that maybe at least this could inspire your solution, you are
    # amazing and please remember that, we have come a long way moctly because of you and
    # your guidance, I appreciate you so much, sorry I did not manage this
    
    # @login_required
    # def edit_post(UpdateView):
    #     """ Editing existing posts """
    #     posts_value = Post.content

    #     if request.method == 'POST':
    #         form = PostForm(request.POST)
    #     try:
    #         if form.is_valid():
    #             form.save
    #             post.user = request.user
    #             messages.success(request, 'Your post was edited')
    #             return redirect(reverse('edit_post'))
        
    #     except Exception as e:
    #         messages.warning(request, 'Your post was not edited this time')
    #     else:
    #         form = PostForm()
    #     context = {
    #         'posts': post
    #     }

    #     return render(request, template, context)