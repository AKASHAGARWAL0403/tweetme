from rest_framework import serializers
from accounts.api.serializers import UserModalSerializers
from tweets.models import Tweet
from django.utils.timesince import timesince

class ParentTweetModalSerializers(serializers.ModelSerializer):
    user = UserModalSerializers(read_only = True)
    timesince = serializers.SerializerMethodField()
    date_display = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'user' ,
            'id', 
            'content',
            'timestamp',
            'date_display',
            'timesince'
            ]
    
    def get_date_display(self , obj):
        return obj.timestamp.strftime("%b %d, %I:%M %p")

    def get_timesince(self,obj):
        return timesince(obj.timestamp) + " ago"

class TweetModalSerializers(serializers.ModelSerializer):
    user = UserModalSerializers(read_only = True)
    timesince = serializers.SerializerMethodField()
    date_display = serializers.SerializerMethodField()
    parent = ParentTweetModalSerializers(read_only = True)
    like_count = serializers.SerializerMethodField()
    user_liked = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user' ,
            'id', 
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'parent',
            'like_count',
            'user_liked'
            ]

    def get_user_liked(self , obj):
        cont = self.context.get('request')
        user = cont.user
        if user in obj.liked.all():
            return True
        return False

    def get_like_count(self , obj):
        return obj.liked.all().count()

    def get_date_display(self , obj):
        return obj.timestamp.strftime("%b %d, %I:%M %p")

    def get_timesince(self,obj):
        return timesince(obj.timestamp) + " ago"
