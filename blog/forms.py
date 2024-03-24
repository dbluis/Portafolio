from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "image", "date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un titulo"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe una descripcion"}),
        }
