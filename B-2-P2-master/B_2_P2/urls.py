"""B_2_P2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # path('', TemplateView.as_view(template_name="index.html")),
    path("", views.main_list, name="main_list"),
    path('logout', LogoutView.as_view()),

    path('admin/', admin.site.urls),
    path('pawn/', include('pawn.urls')),
    path('questions/', include("questions.urls")), 
    path('users/', include('users.urls')), 
    path('communities/', include('communities.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
