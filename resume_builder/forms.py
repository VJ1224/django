from django import forms
from .models import resume


class resumeForm(forms.ModelForm):
    class Meta:
        model = resume
        fields = ['name', 'email', 'number', 'education', 'work', 'skills']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'education': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'work': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'skills': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
