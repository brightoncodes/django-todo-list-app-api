from django import forms
from .models import Todo


class TodoCreateForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={
        'value' : '',
        'type' : 'hidden'
    }))
    class Meta:
        model = Todo
        fields = ['user','title']