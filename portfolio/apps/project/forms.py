from django import forms
from .models import     Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'video', 'thumbnail', 'tools', 'link_project', 'type']
        link_project = forms.CharField(required=False)
