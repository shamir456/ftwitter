from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from .models import Tweet
from django.views.generic import DetailView,ListView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import TweetModelForm 
from .mixims import FormUserNeedMixim,UserOwnerMixin
from django import forms

# Create your views here.

class RetweetView(View):
	"""docstring for ClassName"""
	def get(self,request,pk,*args,**kwargs):
		tweet=get_object_or_404(Tweet,pk=pk)
		if request.user.is_authenticated():
			new_tweet=Tweet.objects.retweet(request.user,tweet)
			return HttpResponseRedirect("/")
		return HttpResponseRedirect(tweet.get_absolute_url())
	

class TweetCreateView(FormUserNeedMixim,CreateView):
	form_class = TweetModelForm
	template_name= 'tweets/create_view.html'


	

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
	queryset = Tweet.objects.all()
	form_class=TweetModelForm
	template_name='tweets/update_view.html'
	success_url='/tweet/'
	
class TweetDeleteView(LoginRequiredMixin,DeleteView):
	queryset = Tweet.objects.all()

	template_name='tweets/delete_confirm.html'
	success_url=reverse_lazy('tweet:list')
	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		if self.request.user == self.object.user:
			success_url = self.get_success_url()
			self.object.delete()
			return HttpResponseRedirect(success_url)
		else:
			
			return HttpResponseRedirect(self.object.get_absolute_url())


	def get_object(self):
		print(self.kwargs)
		pk = self.kwargs.get("pk")
		return Tweet.objects.get(id=pk)

class TweetDetailView(DetailView):
	template_name="tweets/detail_view.html"
	queryset = Tweet.objects.all()
 
	def get_object(self):
		print(self.kwargs)
		pk = self.kwargs.get("pk")
		return Tweet.objects.get(id=pk)
	"""docstring for Clame"""

class TweetListView(ListView):
	"""docstring for TweetListView"""
	#template_name="tweets/list_view.html"
	#queryset = Tweet.objects.all()
	def get_context_data(self,*args,**kwargs):
		context = super(TweetListView,self).get_context_data(*args,**kwargs)
		context['create_form']=TweetModelForm()
		context['create_url']=reverse_lazy('tweet:create')

		return context

	def get_queryset(self,*args,**kwargs):
		qs=Tweet.objects.all()
		query=self.request.GET.get('q',None)
		if query is not None:
			qs=qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
			print(qs)
		return qs
		


