from rest_framework import generics
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions
from tweets.api.pagination import StandardResultPagination 
from tweets.api.serializers import TweetModalSerializers
from hashtag.models import Hashtag

class HashListAPIView(generics.ListAPIView):
    serializer_class = TweetModalSerializers
    pagination_class = StandardResultPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(HashListAPIView, self).get_serializer_context(*args, **kwargs)
        context.update({
            'request' : self.request
        })
        return context

    def get_queryset(self,*args,**kwargs):
        hash_tag = self.kwargs.get("hashtag")
        hash_obj = None
        try:
            hash_obj = Hashtag.objects.get_or_create(tag = hash_tag)[0]
        except:
           pass
        if hash_obj:
            qs = hash_obj.get_tweet()
            query = self.request.GET.get('q',None)
            if query is not None:
                qs = qs.filter(
                    Q(content__icontains=query) | 
                    Q(user__username__icontains=query)
                )
            print(qs)
            return qs
        return None