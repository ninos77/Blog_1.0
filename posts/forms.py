from .models import *
from django import forms
from django.contrib.admin import widgets


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        categories = Category.objects.all()
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Content'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=(categories))


        }

        fields = [
            'title',
            'content',
            'image',
            'category'
        ]
