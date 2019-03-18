from django import forms
from loginapp.models import UserProfileInfo
from django.contrib.auth.models import User
class TodoList(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta():
        model = User
        fields = ('username', 'email')
