from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class bpquestions(models.Model):
	time = models.TimeField(auto_now_add=True)
	name = models.CharField(max_length=100, null=True, blank=True,db_column="Name(Optional)")
	question = models.TextField()
	def __str__(self):
		return self.name


