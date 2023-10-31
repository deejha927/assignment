from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text", "author"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text", "question", "author"]


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ["user", "answer"]
