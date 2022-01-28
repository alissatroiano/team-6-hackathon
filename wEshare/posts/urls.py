from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
]
