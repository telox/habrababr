from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'short_description', 'description',)

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')