from dataclasses import fields
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['description', 'content']
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
   
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows':2,
            'width':'100%',
            'class': 'form-control', 'text-left'
            'placeholder': 'Add an image, quote or video url of your choice!'}))
    
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows':1,
            'width':'100%',
            'class': 'form-control', 'text-center'
            'placeholder': 'Add an image, quote or video url of your choice!'}))