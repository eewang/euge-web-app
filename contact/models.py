from django.db import models
from django.contrib import admin

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	birthday = models.DateTimeField()
	company = models.CharField(max_length=100)	
	context = models.TextField('Intro Context')

	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)	

admin.site.register(Contact)

