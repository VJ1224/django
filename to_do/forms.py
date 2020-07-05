from django import forms
from .models import toDoItem


class toDoForm(forms.ModelForm):
    class Meta:
        model = toDoItem
        fields = ['title', 'category', 'date_due', 'description']
        error_messages = {
            'date_due': {
                'invalid': 'Enter a valid date. Format: YYYY-MM-DD.'
            }
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_due': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '(YYYY-MM-DD)'
                }
            ),
            'category': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
