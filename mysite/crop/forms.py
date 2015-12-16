from django import forms
from .models import Worker

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
