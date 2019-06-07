from django.contrib import admin
from .models import Tweet
from .forms import TweetForm
# Register your models here.


class TweetModelAdmin(admin.ModelAdmin):
    #form = TweetForm
    class Meta:
        model = Tweet

admin.site.register(Tweet , TweetModelAdmin)