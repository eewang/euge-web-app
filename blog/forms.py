from django import forms
from django.forms import ModelForm
from blog.models import *

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False)
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message

class AuthorForm(ModelForm):
	class Meta:
		model = Author

class BlogForm(ModelForm):
	class Meta:
		model = Post
