from django.urls import path, include
from .views import index, view_posts, create_post

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('view_posts/', view_posts, name='view_posts'),
    path('create_post/', create_post, name='create_post'),
]
