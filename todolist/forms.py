from todolist.models import TodoList
from django import forms
from django.core import validators


class AddOrEditItemForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ['content']