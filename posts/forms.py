from .models import *
from django import forms
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        categories = Category.objects.all()
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Content'}),
            'category': forms.Select(attrs={'class': 'form-control '}, choices=(categories))


        }

        fields = [
            'title',
            'content',
            'image',
            'category'
        ]


class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.field_class = 'col-12 p-0 input-group'
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('category', css_class='form-control'),
            Field('content', css_class='form-control'),
            Field('image', css_class='form-control'),
            Field('tag', css_class='form-control',
                  value=self.instance.post_tag())

        )
        self.helper.add_input(
            Submit('submit', 'Update', css_class=('btn primary-button')))
    tag = forms.CharField()

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'category'
        ]
