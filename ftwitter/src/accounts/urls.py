
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView,
    UserFollowView
    )
from django.conf import settings



urlpatterns = [
   

    url(r'^(?P<username>[\w.@+-]+)/$',UserDetailView.as_view(),name='detail'), #api/tweets/
    url(r'^(?P<username>[\w.@+-]+)/follow/$',UserFollowView.as_view(),name='follow'),

]
