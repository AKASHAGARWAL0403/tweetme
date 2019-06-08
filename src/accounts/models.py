from django.db import models
from django.conf import settings
from django.urls import reverse
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
    
    def to_toggle_user(self , user , toggle_user):
        user_profile , created = UserModel.objects.get_or_create(user=user)
        added = False
        if toggle_user in user_profile.following.all():
            user_profile.following.remove(toggle_user)
            added = False
        else:
            user_profile.following.add(toggle_user)
            added = True
        return added

    def is_following(self , user , toggle_user):
        user_profile , created = UserModel.objects.get_or_create(user=user)
        if toggle_user in user_profile.following.all():
            return True
        else:
            return False

class UserModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , related_name="profile" , on_delete=models.CASCADE)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL , related_name="followed_by" , blank=True)

    objects = UserProfileManager()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username = self.user.username)

    def get_follow_url(self):
        return reverse("profile:follow" , kwargs={"username" : self.user.username})

    def get_absolute_url(self):
        return reverse("profile:user_profile" , kwargs={"username" : self.user.username})
