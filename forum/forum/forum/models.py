from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post_title = models.CharField(max_length = 200)
	post_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published', default=datetime.now())

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	def __str__(self):
		return self.post_title

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length = 200)

	def __str__(self):
		return self.comment_text

