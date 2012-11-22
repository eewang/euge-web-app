from django import forms
from django.forms import ModelForm
from contact.models import *

class ContactListForm(ModelForm):
	class Meta:
		model = Contact

