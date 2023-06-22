from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse


class Todo(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	date_created = models.DateTimeField(default=timezone.now)
	label = models.CharField(max_length=100, default='')
	tasks = models.TextField()
	Check_if_task_is_completed =  models.BooleanField(default=False)

	def __str__(self):
		return self.label

	# def get_absolute_url(self):
	# 	return reverse('tasks', kwargs={'id': self.id})

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username
