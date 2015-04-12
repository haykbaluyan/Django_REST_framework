from django.db import models

# Create your models here.

class Snippet(models.Model):
	name = models.CharField(max_length = 100, blank = True, default = 'defName')
	title = models.CharField(max_length = 1000, blank = True, default = 'defTitle')
	age = models.IntegerField(max_length = 5, blank = True, default = 0)
	
