from django.shortcuts import render
from allauth.account.forms import LoginForm
from allauth.account.views import SignupView

# Create your views here.
def index(request):
    """ A view to return the index page """
    template = 'index.html'
    context ={
        'LoginForm': LoginForm,
        'SignupView': SignupView,
    }
    return render(request, template, context)
