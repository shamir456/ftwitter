from rest_framework import serializers
from  django.utils.timesince import timesince
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer

class  ParentModelSerializer(serializers.ModelSerializer):
	user=UserDisplaySerializer(read_only=True)
	date_display= serializers.SerializerMethodField()
	timesince= serializers.SerializerMethodField()
	
	class Meta:
		model = Tweet
		fields = [
		'id',
		'user',
		'content',
		'image',
		'timestamp',
		'date_display',
		'timesince',
		]

	
	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d %I:%M %p")		
	
	def get_timesince(self, obj):
		return timesince(obj.timestamp) + " ago"	

class  TweetModelSerializer(serializers.ModelSerializer):
	user=UserDisplaySerializer(read_only=True)
	date_display= serializers.SerializerMethodField()
	timesince= serializers.SerializerMethodField()
	parent=ParentModelSerializer(read_only=True)
	likes=serializers.SerializerMethodField()
	did_like=serializers.SerializerMethodField()
	class Meta:
		model = Tweet
		fields = [
		'id',
		'user',
		'content',
		'image',
		'timestamp',
		'date_display',
		'timesince',
		'parent',
		'likes',
		'did_like',
		]

	def get_did_like(self, obj):
       		request = self.context.get("request")
       		try:
       			user = request.user
       			if user.is_authenticated():
       				if user in obj.liked.all():
       					return True
              
       		except:
       			pass
       		return False
       			
  


	def get_likes(self,obj):
		return obj.liked.all().count()
	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d %I:%M %p")		
	
	def get_timesince(self, obj):
		return timesince(obj.timestamp) + " ago"	