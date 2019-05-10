from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
class TweetManager(models.Manager):
	def retweet(self,user,parent_obj):
		if parent_obj.parent:
			og_parent=parent_obj.parent
		else:
			og_parent=parent_obj

		qs=self.get_queryset().filter(user=user,parent=og_parent)
		if qs.exists():
			return None
		obj=self.model(
			parent=og_parent,
			user=user,
			content=parent_obj.content,
			image=parent_obj.image,

			)
		obj.save()

		return obj

	def like_toggle(self,user,tweet_obj):
		if user in tweet_obj.liked.all():
			is_liked=False
			tweet_obj.liked.remove(user)
		else:
		    is_liked=True
		    tweet_obj.liked.add(user)
		return is_liked		


		

class Tweet(models.Model):



	user =models.ForeignKey(settings.AUTH_USER_MODEL)
	parent = models.ForeignKey("self",blank=True,null=True)
	content = models.CharField(max_length=140)
	timestamp=models.DateTimeField(auto_now_add=True)
	liked=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='liked') 
	updated=models.DateTimeField(auto_now=True)
	image = models.FileField(upload_to='images',blank=True)

	objects=TweetManager()


	def __str__(self):
		return str(self.content)
		
	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})

	class Meta:
		ordering = ['-timestamp']
		
			

