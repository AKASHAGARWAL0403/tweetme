from django.conf.urls import url
from tweets.api.views import TweetListAPIView

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/tweet/$' , TweetListAPIView.as_view() , name='api-user-profile'),
    # url(r'create/$' , TweetCreateView.as_view()  , name="create_view"),
    # url(r'update/(?P<pk>\d+)/$' , TweetUpdateView.as_view() , name = "update_view"),
    # url(r'delete/(?P<pk>\d+)/$' , TweetDeleteView.as_view() , name = "delete_view"), 
]