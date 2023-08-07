from django import forms
from .models import hockey
class hockeyForm(forms.ModelForm):
    class Meta:
        model = hockey
        fields = '__all__'