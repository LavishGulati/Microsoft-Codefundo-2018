from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Register(models.Model):
	name = models.CharField(max_length=300)
	contact = models.CharField(max_length=300)
	profession = models.CharField(max_length=300)
	location = models.CharField(max_length=100)
	message = models.CharField(max_length=300)

	def __str__(self):
		return self.name