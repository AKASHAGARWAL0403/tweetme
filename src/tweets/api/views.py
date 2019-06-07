from rest_framework import generics
from .serializers import TweetModalSerializers
from tweets.models import Tweet


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModalSerializers

    def get_queryset(self,*args,**kwargs):
        return Tweet.objects.all() 


