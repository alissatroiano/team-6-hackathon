from django.contrib import admin
from django.urls import path, include

# Define project-wide urls here. https://coderwall.com/p/aey-rq/django-allauth-quick-setup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('posts.urls'), name="posts"),
    path('posts/', include('posts.urls'), name="posts"),
]
