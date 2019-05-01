
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (
	# TweetDetailView,
	# TweetListView,
	# TweetCreateView,TweetUpdateView,
	# TweetDeleteView
    TweetListAPIView
    )
from django.conf import settings



urlpatterns = [
   
#    url(r'^$',RedirectView.as_view(url='/')),
     url(r'^$',TweetListAPIView.as_view(),name='list'), #api/tweets/
#     url(r'^create/$',TweetCreateView.as_view(),name='create'),
#     url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'), #/tweet/1/detail
#     url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),  #/tweet/1/update
#     url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), #/tweet/1/delete
# ]
]
