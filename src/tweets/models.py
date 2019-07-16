from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class TweetManager(models.Manager):
    def retweet(self , user , parent_obj , *args , **kwargs):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj
        qs = self.get_queryset().filter(user=user , parent = og_parent)
        
        if qs.exists():
            return None

        obj = self.model(
            parent = og_parent , 
            user = user , 
            content = og_parent.content
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
    is_reply = models.BooleanField(verbose_name='Is a reply?', default=False)
    content = models.CharField(max_length=140)
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

    def get_parent(self):
        parent = self
        if self.parent:
            parent = self.parent
        return parent

    def get_children(self):
        parent = self.get_parent()
        qs1 = Tweet.objects.filter(parent = parent)
        qs2 = Tweet.objects.filter(pk=parent.pk)
        return (qs1 | qs2)
