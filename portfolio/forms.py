from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "image", "url"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un titulo"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe una descripcion"}),
        }
