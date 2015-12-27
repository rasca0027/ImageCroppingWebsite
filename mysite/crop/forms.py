from django import forms
from .models import Worker

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        users = Worker.objects.filter(username=cleaned_data['username'])
        if users.count() > 0:
            raise ValidationError("The username has already been registered."
                                  " Please try another one.")
        return cleaned_data
