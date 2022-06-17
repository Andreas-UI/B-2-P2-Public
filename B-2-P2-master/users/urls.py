from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path("logout", views.logout_request, name="logout"),
    path("<pk>/<username>/sorted", views.users_detail, name="users_detail"),
    path("update", views.users_update, name="users_update"),
    path("<pk>/<username>/reverse", views.users_detail_reverse, name="users_detail_reverse"),
    path("<pk>/<username>/solved", views.users_detail_solved, name="users_detail_solved"),
    path("<pk>/<username>/unsolved", views.users_detail_unsolved, name="users_detail_unsolved"),
    path("<pk>/<username>/connect", views.users_detail_connect, name="users_detail_connect"),
    
    path("<pk>/<username>/answers/sorted", views.users_detail_answers, name="users_detail_answers"),
    path("<pk>/<username>/answers/reverse", views.users_detail_answers_reverse, name="users_detail_answers_reverse"),
    path("<pk>/<username>/answers/pinned", views.users_detail_answers_pinned, name="users_detail_answers_pinned"),
    path("<pk>/<username>/answers/unpinned", views.users_detail_answers_unpinned, name="users_detail_answers_unpinned"),

    path("<pk>/<username>/neighbors/follower", views.users_detail_follower, name="users_detail_follower"),
    path("<pk>/<username>/neighbors/following", views.users_detail_following, name="users_detail_following"),

    path("bookmark", views.users_detail_bookmark, name="users_detail_bookmark"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)