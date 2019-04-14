
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (
	TweetDetailView,
	TweetListView,
	TweetCreateView,tweet_create_view)
from django.conf import settings

urlpatterns = [
   
    url(r'^$',TweetListView.as_view(),name='list'), #/tweets/
    url(r'^create/$',tweet_create_view,name='create'),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'), #/tweet/1
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

