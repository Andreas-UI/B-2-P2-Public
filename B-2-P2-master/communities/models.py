from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

import random

# Create your models here.
class Community(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community_name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to="community/community_name/%Y/%m/%d/")
    description = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=480, blank=True)
    member = models.ManyToManyField(User, blank=True, related_name="member")

    class Category(models.IntegerChoices):
        RANDOM = 0, "Random"
        MOVIE = 1, "Movie"
        MUSIC = 2, "Music"
        NEWS = 3, "News"
        CELEBRITY = 4, "Celebrity"
        TV_SHOWS = 5, "TV Shows"
        GAMES = 6, "Games"
        GENERAL = 7, "General"
        BUSINESS = 8, "Business"
        SPORTS = 9, "Sports"
        ACADEMIC = 10, "Academic"
        SOCIAL = 11, "Social"

    category = models.PositiveSmallIntegerField(
        choices=Category.choices,
        default=Category.RANDOM
    )

    def __str__(self):
        return self.community_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.community_name)
        super(Community, self).save(*args, **kwargs)