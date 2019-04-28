from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Tweet(models.Model):

	user =models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.CharField(max_length=140)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	image = models.FileField(upload_to='images',blank=True)

	def __str__(self):
		return str(self.content)
		
	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})

