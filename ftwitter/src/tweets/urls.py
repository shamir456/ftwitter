
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (
	TweetDetailView,
	TweetListView,
	TweetCreateView,TweetUpdateView,
	TweetDeleteView)
from django.conf import settings

from django.views.generic.base import RedirectView

urlpatterns = [
   
   url(r'^$',RedirectView.as_view(url='/')),
    url(r'^search/$',TweetListView.as_view(),name='list'), #/tweets/
    url(r'^create/$',TweetCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'), #/tweet/1/detail
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),  #/tweet/1/update
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), #/tweet/1/delete
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

