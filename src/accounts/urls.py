from django.conf.urls import url
from .views import UserProfileView

app_name = "profile"
urlpatterns = [
   url(r'^(?P<username>[\w.@+-]+)/$', UserProfileView.as_view()  , name="user_profile"),
]
