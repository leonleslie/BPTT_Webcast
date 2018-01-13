from .models import bpquestions
from django import forms

class questionform(forms.ModelForm):
	class Meta:
		model = bpquestions
		fields = [
			'name',
			'question',
			

		]
