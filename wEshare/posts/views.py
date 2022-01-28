from django.shortcuts import render
from allauth.account.forms import LoginForm


# Create your views here.
def index(request):
    """ A view to return the index page """
    template = 'index.html'
    context ={
        'LoginForm': LoginForm,
    }
    return render(request, template, context)
