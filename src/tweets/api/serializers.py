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
    class Meta:
        model = Tweet
        fields = [
            'user' ,
            'id', 
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'parent'
            ]
    
    def get_date_display(self , obj):
        return obj.timestamp.strftime("%b %d, %I:%M %p")

    def get_timesince(self,obj):
        return timesince(obj.timestamp) + " ago"
