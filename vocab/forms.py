from django import forms
from django.forms import ModelForm
from vocab.models import *

class VocabListForm(ModelForm):
	class Meta:
		model = Vocab
