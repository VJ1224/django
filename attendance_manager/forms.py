from django import forms
from .models import Course

class courseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['code','title']
        widgets = {
            'code': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
			}
