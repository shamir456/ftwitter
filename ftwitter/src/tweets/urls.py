
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (
	TweetDetailView,
	TweetListView,
	TweetCreateView)
from django.conf import settings

urlpatterns = [
   
    url(r'^$',TweetListView.as_view(),name='list'), #/tweets/
    url(r'^create/$',TweetCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'), #/tweet/1
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

