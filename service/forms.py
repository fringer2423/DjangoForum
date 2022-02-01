from django.forms import ModelForm
from .models import Post, Comment, Message
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {"title": forms.TextInput(attrs={'class': 'form-control'}),
                   "description": forms.Textarea(attrs={'class': 'form-control'}),
                   }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["description"]
        widgets = {"description": forms.Textarea(attrs={'class': 'form-control'})}


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["title", 'body']
        widgets = {"title": forms.TextInput(attrs={'class': 'form-control'}),
                   "body": forms.Textarea(attrs={'class': 'form-control'}),
                   }
