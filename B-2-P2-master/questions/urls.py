from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path("", views.questions_list, name="questions_list"),
    path("ask/", views.questions_ask, name="questions_ask"),
    path("search/", views.questions_search, name="questions_search"),
    path("tags/<tag>", views.questions_tag, name="questions_tag"),
    path("category/<category>", views.questions_category, name="questions_category"),

    path("<pk>/<slug>", views.questions_detail, name="questions_detail"),
    path("<pk>/<slug>/update", views.questions_detail_update, name="questions_detail_update"),
    path("<pk>/<slug>/delete", views.questions_delete, name="questions_delete"),
    path("<pk>/<slug>/bookmark", views.questions_detail_bookmark, name="questions_detail_bookmark"),
    path("<pk>/<slug>/thumbsup", views.questions_detail_thumbsup, name="questions_detail_thumbsup"),
    path("<pk>/<slug>/thumbsdown", views.questions_detail_thumbsdown, name="questions_detail_thumbsdown"),
    path("<pk>/<slug>/<comment_pk>/pin", views.questions_detail_pin, name="questions_detail_pin"),
    path("<pk>/<slug>/<comment_pk>/upvote", views.questions_comment_upvote, name="questions_comment_upvote"),
    path("<pk>/<slug>/<comment_pk>/downvote", views.questions_comment_downvote, name="questions_comment_downvote"),
    path("<pk>/<slug>/<comment_pk>/edit", views.questions_comment_edit, name="questions_comment_edit"),
    path("<pk>/<slug>/<comment_pk>/delete", views.questions_comment_delete, name="questions_comment_delete"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)