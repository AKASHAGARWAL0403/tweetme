from django.conf.urls import url
from .views import TweetListAPIView
from django.views.generic.base import RedirectView

app_name = "api-tweets"
urlpatterns = [
     url(r'^$' , TweetListAPIView.as_view() , name="list_view"),
    # url(r'search/$', TweetListView.as_view() , name="list_view"),
    # url(r'create/$' , TweetCreateView.as_view()  , name="create_view"),
    # url(r'update/(?P<pk>\d+)/$' , TweetUpdateView.as_view() , name = "update_view"),
    # url(r'delete/(?P<pk>\d+)/$' , TweetDeleteView.as_view() , name = "delete_view"),
    # url(r'^(?P<pk>\d+)/$' , TweetDetailView.as_view()  , name="detail_view"),
]
