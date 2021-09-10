from django import forms
from django.db.models import fields
from .models import Image, Post
from django.forms import ModelForm, widgets

class ImageForm(ModelForm):
    class Meta:
        model= Image
        fields= "__all__"

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        
        widgets ={
            'tags': forms.CheckboxSelectMultiple()
        }

