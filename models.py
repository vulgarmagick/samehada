from django.db import models
from django.utils import timezone

# Create your models here.

# Quotes 
class Quote(models.Model):
	text = models.TextField(max_length=200, null=True)
	source = models.CharField(max_length=50, null=True)
	when = models.DateTimeField(blank=True, null=True)
	
	def quote (self): 
		self.save

		
	def _str_ (self):
		return self.when
	
