from django.conf.urls import url
from .views import MarkdownifyView, ImageUploadView
from django.urls import path

urlpatterns = [
    path('markdownify/', MarkdownifyView.as_view(), name='pawn_markdownify'),
    path('upload/', ImageUploadView.as_view(), name='pawn_upload')
]
