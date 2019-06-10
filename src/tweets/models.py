from django.db import models
from django.conf import settings
from .validators import validate_content
from django.urls import reverse
# Create your models here.

class TweetManager(models.Manager):
    def retweet(self , user , parent , *args , **kwargs):
        if parent.parent:
            parent = parent.parent
        
        qs = self.get_queryset().filter(user=user , parent = parent)
        
        if qs.exists():
            return None

        obj = self.model(
            parent = parent , 
            user = user , 
            content = parent.content
        )
        obj.save()
        return obj

    def is_liked(self , user , tweet_obj , *args , **kwargs):
        if user in  tweet_obj.liked.all():
            is_like = False
            tweet_obj.liked.remove(user)
        else:
            is_like = True
            tweet_obj.liked.add(user)
        return is_like    

class Tweet(models.Model):
    parent = models.ForeignKey("self" , on_delete = models.CASCADE , blank = True , null = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL , related_name="liked" , blank=True)
    content = models.CharField(max_length=140 , validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = TweetManager()

    # def clean(self,*args,**kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("It cannot be abc")
    #     return super(Tweet,self).clean(*args,**kwargs)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweets:detail_view" , kwargs={"pk":self.pk})