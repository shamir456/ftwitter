from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tweet
from django.views.generic import DetailView,ListView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TweetModelForm 
from .mixims import FormUserNeedMixim,UserOwnerMixin
# Create your views here.
class TweetCreateView(LoginRequiredMixin,FormUserNeedMixim,CreateView):
	form_class = TweetModelForm
	template_name= 'tweets/create_view.html'
	success_url = "/tweet/create/"
	login_url = '/admin/'

	

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
	queryset = Tweet.objects.all()
	form_class=TweetModelForm
	template_name='tweets/update_view.html'
	success_url='/tweet/'
	
class TweetDeleteView(LoginRequiredMixin,DeleteView):
	model =Tweet
	template_name='tweets/delete_confirm.html'
	success_url=reverse_lazy('home')
	
		

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
	template_name="tweets/list_view.html"
	queryset = Tweet.objects.all()
		


# def tweet_detail_veiw(request,id=5):
# 	obj= Tweet.objects.get(id=id)
# 	print(obj.content)
# 	context = {
# 	   "object" : obj
# 	}
# 	return render(request,"tweets/detail_veiw.html",context)


# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	context = {
# 	   "object_list":queryset
# 	}
# 	for i in queryset:
# 		print(i.content)
# 		print(i.image)
# 	return render(request,"tweets/list_view.html",context)