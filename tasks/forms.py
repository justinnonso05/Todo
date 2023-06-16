from django import forms
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class AddTodoForm(forms.ModelForm):
	tasks = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
	class Meta:
		model = Todo
		fields = ['label', 'tasks']

class DeleteTaskForm(forms.Form):
	some_input = forms.IntegerField(widget=forms.HiddenInput(), required = False)