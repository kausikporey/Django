# forms.py 
from django import forms 
from .models import Person

class ImageForm(forms.ModelForm): 
	
	class Meta: 
		model = Person 
		fields = ['image'] 
