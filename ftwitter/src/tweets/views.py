from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Tweet
from django.views.generic import DetailView,ListView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TweetModelForm 
from .mixims import FormUserNeedMixim,UserOwnerMixin
# Create your views here.
class TweetCreateView(FormUserNeedMixim,CreateView):
	form_class = TweetModelForm
	template_name= 'tweets/create_view.html'
	#success_url = reverse_lazy("tweet:detail")
	#login_url = '/admin/'

	

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
	queryset = Tweet.objects.all()
	form_class=TweetModelForm
	template_name='tweets/update_view.html'
	success_url='/tweet/'
	
class TweetDeleteView(LoginRequiredMixin,DeleteView):
	model =Tweet
	template_name='tweets/delete_confirm.html'
	success_url=reverse_lazy('tweet:list')
	
		

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
		print(self.request.GET)
		query=self.request.GET.get('q',None)
		if query is not None:
			qs=qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
			print(qs)
		return qs
		


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