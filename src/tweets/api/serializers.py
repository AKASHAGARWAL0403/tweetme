from rest_framework import serializers
from accounts.api.serializers import UserModalSerializers
from tweets.models import Tweet

class TweetModalSerializers(serializers.ModelSerializer):
    user = UserModalSerializers()
    class Meta:
        model = Tweet
        fields = ['user' , 'content']