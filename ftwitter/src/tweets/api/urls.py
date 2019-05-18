
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (
	RetweetAPIView,
	TweetCreateAPIView,
    TweetListAPIView,
    LikeToggleAPIView
    )
from django.conf import settings



urlpatterns = [
   

     url(r'^$',TweetListAPIView.as_view(),name='list'), #api/tweets/
     url(r'^create/$',TweetCreateAPIView.as_view(),name='create'),
     url(r'^search/$',TweetCreateAPIView.as_view(),name='search-api'),
     url(r'^(?P<pk>\d+)/retweet/$',RetweetAPIView.as_view(),name='retweet'),
     url(r'^(?P<pk>\d+)/like/$',LikeToggleAPIView.as_view(),name='like-toggle'),

]
