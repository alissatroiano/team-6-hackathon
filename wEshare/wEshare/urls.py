from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# Define project-wide urls here. https://coderwall.com/p/aey-rq/django-allauth-quick-setup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
