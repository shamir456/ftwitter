from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from tweets.models import Tweet
from .serializers import TweetModelSerializer
from .pagination import StandardResultsPagination


class LikeToggleAPIView(APIView):
	permission_classes=[permissions.IsAuthenticated]
	def get(self,request,pk,format=None):
		tweet_qs=Tweet.objects.filter(pk=pk)
		message="Not allowed"
		if request.user.is_authenticated():
			is_liked=Tweet.objects.like_toggle(request.user,tweet_qs.first())
			return Response({'liked':is_liked})
		return Response({"message":message},status=400)


class RetweetAPIView(APIView):
	permission_classes=[permissions.IsAuthenticated]
	def get(self,request,pk,format=None):
		return Response(True)

class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class= TweetModelSerializer
	permission_classes = [permissions.IsAuthenticated ]

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)



class SearchTweetAPIView(generics.ListAPIView):
	queryset= Tweet.objects.all().order_by("-timestamp")
	serializer_class= TweetModelSerializer
	pagination_class=StandardResultsPagination

	def get_serializer_context(self,*args,**kwargs):
		context = super(SearchTweetAPIView, self).get_serializer_context(*args,**kwargs)
		context['request']=self.request
		return context
	def get_queryset(self,*args,**kwargs):
		qs = self.queryset
		query = self.request.GET.get("q", None)
		if query is not None:
			qs=qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
		return qs


class TweetListAPIView(generics.ListAPIView):
	serializer_class= TweetModelSerializer
	pagination_class=StandardResultsPagination

	def get_serializer_context(self,*args,**kwargs):
		context = super(TweetListAPIView, self).get_serializer_context(*args,**kwargs)
		context['request']=self.request
		return context

	def get_queryset(self,*args,**kwargs):
		im_following=self.request.user.profile.get_following()
		qs1=Tweet.objects.filter(user__in=im_following)
		qs2=Tweet.objects.filter(user=self.request.user)
		qs=(qs1 | qs2).distinct().order_by("-timestamp")
		query=self.request.GET.get('q',None)
		if query is not None:
			qs=qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
		return qs

class SearchAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by("-timestamp")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs
		
