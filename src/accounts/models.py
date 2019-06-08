from django.db import models
from django.conf import settings
# Create your models here.

class UserProfileManager(models.Manager):
    def all(self):
        queryset = self.get_queryset().all()
        try:
            if self.instance:
                queryset = queryset.exclude(user = self.instance)
        except:
            pass
        return queryset

class UserModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , related_name="profile" , on_delete=models.CASCADE)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL , related_name="followed_by" , blank=True)

    objects = UserProfileManager()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all();
        return users.exclude(username = self.user.username)

