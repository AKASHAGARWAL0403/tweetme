from rest_framework import generics
from .serializers import TweetModalSerializers
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardResultPagination 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TweetModalSerializers
from django.contrib.auth.mixins import LoginRequiredMixin

class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self , request , pk , *args , **kwargs):
        tweet_obj = Tweet.objects.filter(pk = pk)
        message = "Not Allowed"
        if request.user.is_authenticated:
            is_liked = Tweet.objects.is_liked(request.user , tweet_obj.first())
            return Response({'liked' : is_liked})
        return Response({'message' : message} , status=400)


class RetweetView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self , request , pk , format=None):
        par_obj = Tweet.objects.filter(pk = pk)
        message = "Not allowed"
        if par_obj.exists() and par_obj.count() == 1:
            #if request.user.is_authenticated:
            retweet_obj = Tweet.objects.retweet(request.user , par_obj.first())
            if retweet_obj is not None:
                ser_data = TweetModalSerializers(retweet_obj).data
                return Response(ser_data)
            message = "User cant retweet it more than once"

        return Response({"message" : message} , status=400)

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModalSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request)
        serializer.save(user=self.request.user)


# class TweetDetailAPIView(generics.RetrieveAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetModalSerializers
#     permission_classes = [permissions.AllowAny]


class TweetDetailAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetModalSerializers
    pagination_class = StandardResultPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self , *args , **kwargs):
        tweet_id = self.kwargs.get("pk")
        qs = Tweet.objects.filter(pk=tweet_id)
        if qs.exists() and qs.count() == 1:
            parent = qs.first()
            qs1 = parent.get_children()
            qs = (qs | qs1).distinct().extra(select={"parent_id_null" : "parent_id IS NULL"})
        #print(qs)
        return qs.order_by('-parent_id_null' , '-timestamp')


class SearchListAPIView(generics.ListAPIView):
    serializer_class = TweetModalSerializers
    pagination_class = StandardResultPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(SearchListAPIView, self).get_serializer_context(*args, **kwargs)
        context.update({
            'request' : self.request
        })
        return context

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all().order_by("-timestamp")
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) | 
                Q(user__username__icontains=query)
            )
        return qs

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModalSerializers
    pagination_class = StandardResultPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context.update({
            'request' : self.request
        })
        return context
    
    def get_queryset(self,*args,**kwargs):
        is_personal = self.kwargs.get("username")
        if is_personal:
            qs = Tweet.objects.filter(user__username = self.kwargs.get("username"))
        else:    
            is_following = self.request.user.profile.get_following()
            qs1 = Tweet.objects.filter(user__in=is_following)
            qs2 = Tweet.objects.filter(user = self.request.user)
            qs = ( qs1 | qs2 ).order_by("-timestamp")
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) | 
                Q(user__username__icontains=query)
            )
        return qs


