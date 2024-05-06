from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Question
        fields = ['text', 'image']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['name', 'text']
