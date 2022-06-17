from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile-picture/user.username/%Y/%m/%d/")
    about = models.TextField(max_length=195, blank=True, null=True)
    neighbors = models.ManyToManyField(User, blank=True, related_name='neighbors')

    def __str__(self):
        return self.user.username