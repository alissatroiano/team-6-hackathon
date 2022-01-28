from django.urls import path

from .views import posts

urlpatterns = [
    path('', posts, name='posts'),
]
