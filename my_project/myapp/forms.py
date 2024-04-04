from django import forms
from .models import subject

class subjectform(forms.ModelForm):
    class Meta:
        model = subject
        fields = '__all__'

