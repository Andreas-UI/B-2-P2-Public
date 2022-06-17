from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path("", views.communities_list, name="communities_list"),
    path("create/", views.communities_create, name="communities_create"),
    path("search/", views.communities_search, name="communities_search"),
    path("detail/<pk>/<slug:slug>/", views.communities_detail, name="communities_detail"),
    path("detail/<pk>/<slug:slug>/delete", views.communities_delete, name="communities_delete"),
    path("detail/<pk>/<slug:slug>/popular", views.communities_detail_popular, name="communities_detail_popular"),
    path("detail/<pk>/<slug:slug>/ask", views.communities_ask, name="communities_ask"),
    path("detail/<pk>/<slug:slug>/join", views.communities_join, name="communities_join"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)