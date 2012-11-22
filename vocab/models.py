from django.db import models
from django.contrib import admin

class Vocab(models.Model):
	word = models.CharField(max_length=50)
	definition = models.TextField()
	synonym = models.TextField('Synonyms')
	antonym = models.TextField('Antonyms')
#	example = models.TextField('Example Sentence')

	def __str__(self):
		return "%" % (self.word) 

admin.site.register(Vocab)

