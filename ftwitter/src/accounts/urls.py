
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView,
    UserFollowView
    )
from django.conf import settings



urlpatterns = [
   
#    url(r'^$',RedirectView.as_view(url='/')),
    
     url(r'^(?P<username>[\w.@+-]+)/$',UserDetailView.as_view(),name='detail'), #api/tweets/
    url(r'^(?P<username>[\w.@+-]+)/follow/$',UserFollowView.as_view(),name='follow'),
#    url(r'^create/$',TweetCreateAPIView.as_view(),name='create'),
#     url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(),name='detail'), #/tweet/1/detail
#     url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),  #/tweet/1/update
#     url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), #/tweet/1/delete
# ]
]
