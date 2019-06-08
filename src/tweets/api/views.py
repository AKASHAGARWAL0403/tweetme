from rest_framework import generics
from .serializers import TweetModalSerializers
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardResultPagination 

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModalSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModalSerializers
    pagination_class = StandardResultPagination
    
    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all().order_by("-timestamp")
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) | 
                Q(user__username__icontains=query)
            )
        return qs


