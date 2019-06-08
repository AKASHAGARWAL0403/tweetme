from django.conf.urls import url
from .views import UserProfileView , UserFollowView

app_name = "profile"
urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserProfileView.as_view()  , name="user_profile"),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view()  , name="follow"),
]
