from django import forms
from todo.models import Task
from django.contrib.auth.models import User


class UserListForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='USER', required=False)

    class Meta:
        model = Task
        fields = ['user']
