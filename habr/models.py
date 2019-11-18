from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=50)
	short_description = models.CharField(max_length=250)
	description = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	published_date = models.DateTimeField(blank=True, null=True)
	#rating = 

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
	description = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	published_date = models.DateTimeField(blank=True, null=True)
	#rating = 

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
