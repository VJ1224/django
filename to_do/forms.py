from django import forms
from .models import toDoItem

class toDoForm(forms.ModelForm):
    class Meta:
        model=toDoItem
        fields=['title','category','date_due','description']
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'description': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
            'date_due': forms.DateInput(
                    format=('%d-%m-%Y'),
    				attrs={
    					'class': 'form-control'
    					}
    				),
            'category': forms.TextInput(
    				attrs={
    					'class': 'form-control'
    					}
    				),
		}
