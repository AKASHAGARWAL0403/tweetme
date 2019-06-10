from django.conf.urls import url
from .views import TweetListAPIView , TweetCreateAPIView , RetweetView , LikeToggleAPIView , TweetDetailAPIView
from django.views.generic.base import RedirectView

app_name = "api-tweets"
urlpatterns = [
    url(r'^$' , TweetListAPIView.as_view() , name="list_view"),
    url(r'create/$', TweetCreateAPIView.as_view() , name="create_view"),
    url(r'^(?P<pk>\d+)/$' , TweetDetailAPIView.as_view()  , name="detail_view"),
    url(r'^(?P<pk>\d+)/retweet/$' , RetweetView.as_view()  , name="retweet_view"),
    url(r'^(?P<pk>\d+)/like/$' , LikeToggleAPIView.as_view()  , name="like_toggle_view"),
    # url(r'create/$' , TweetCreateView.as_view()  , name="create_view"),
    # url(r'update/(?P<pk>\d+)/$' , TweetUpdateView.as_view() , name = "update_view"),
    # url(r'delete/(?P<pk>\d+)/$' , TweetDeleteView.as_view() , name = "delete_view"), 
]