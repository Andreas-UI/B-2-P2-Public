from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from pawn.models import PawnField
from taggit.managers import TaggableManager
from django.utils import timezone
from communities.models import Community

# for reverse lookup 
# https://docs.djangoproject.com/en/2.0/topics/db/queries/#related-objects

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=280)
    summary = models.TextField(max_length=380)
    slug = models.SlugField(max_length=480, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    solved = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    thumbsup = models.ManyToManyField(User, blank=True, related_name='question_thumbsup')
    thumbsdown = models.ManyToManyField(User, blank=True, related_name='question_thumbsdown')

    viewed = models.ManyToManyField(User, blank=True, related_name='viewed')
    bookmark = models.ManyToManyField(User, blank=True, related_name='bookmark')

    noc = models.CharField(max_length=100, default="question")

    community = models.ForeignKey(Community, on_delete=models.CASCADE, blank=True, null=True)

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
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    @property
    def get_vote(self):
        return str(self.thumbsup.count() - self.thumbsdown.count())

    @property
    def type(self):
        return "question"

    @property
    def get_time_delta(self):
        delta = timezone.now() - self.created_on
        seconds = delta.total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)

        days = delta.days
        weeks = int(days // 4)
        months = int(days // 29.53)
        years = int(days // 365.25)

        if years > 0:
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

        if months > 0:
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if weeks > 0:
            if weeks == 1:
                return str(weeks) + " week ago"
            else:
                return str(weeks) + " weeks ago"
            
        if days > 0:
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if hours > 0:
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        if minutes > 0:
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        else:
                return str(seconds) + " seconds ago"

class QuestionComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = PawnField()
    created_on = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    upvote = models.ManyToManyField(User, blank=True, related_name='questioncomment_upvote')
    downvote = models.ManyToManyField(User, blank=True, related_name='questioncomment_downvote')

    def __str__(self):
        return self.question.title + "/" + self.user.username + "/" + str(self.id)

    @property
    def get_vote(self):
        vote = self.upvote.all().count() - self.downvote.all().count()
        return "{}".format(vote)

    @property
    def get_time_delta(self):
        delta = timezone.now() - self.created_on
        seconds = delta.total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)

        days = delta.days
        weeks = int(days // 4)
        months = int(days // 29.53)
        years = int(days // 365.25)

        if years > 0:
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

        if months > 0:
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if weeks > 0:
            if weeks == 1:
                return str(weeks) + " week ago"
            else:
                return str(weeks) + " weeks ago"
            
        if days > 0:
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if hours > 0:
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        if minutes > 0:
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        else:
                return str(seconds) + " seconds ago"


class ReplyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(QuestionComment, on_delete=models.CASCADE)
    reply = models.TextField(max_length=380)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "/" + str(self.id)

    @property
    def get_time_delta(self):
        delta = timezone.now() - self.created_on
        seconds = delta.total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)

        days = delta.days
        weeks = int(days // 4)
        months = int(days // 29.53)
        years = int(days // 365.25)

        if years > 0:
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

        if months > 0:
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if weeks > 0:
            if weeks == 1:
                return str(weeks) + " week ago"
            else:
                return str(weeks) + " weeks ago"
            
        if days > 0:
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if hours > 0:
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        if minutes > 0:
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        else:
                return str(seconds) + " seconds ago"
