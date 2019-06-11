"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from .views import home_view , SearchView
from tweets.views import TweetListView
from hashtag.views import HashtagView
from hashtag.api.views import HashListAPIView 
from tweets.api.views import SearchListAPIView

urlpatterns = [
    url(r'^$', TweetListView.as_view() , name="home"),
    url(r'^search/$', SearchView.as_view() , name="search"),
    url(r'^tweet/',include('tweets.urls'),name ="tweets"),
    url(r'^api/tweet/' , include('tweets.api.urls') , name="api-tweets"),
    url(r'^api/tag/(?P<hashtag>.*)/$' , HashListAPIView.as_view() , name="api-hashtag"),
    url(r'^api/search/' , SearchListAPIView.as_view() , name="api-search"),
    url(r'^api/' , include('accounts.api.urls') , name="api-profile"),
    url(r'^admin/', admin.site.urls),
    url(r'^tags/(?P<hashtag>.*)/$', HashtagView.as_view(), name='hashtag'),
    url(r'^' , include('accounts.urls') , name="profile"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)