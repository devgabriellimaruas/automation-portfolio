from django import forms
from .models import Tools

class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = ['name', 'order']
