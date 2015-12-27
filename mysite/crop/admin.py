from django.contrib import admin
from crop.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    class Meta(UserCreationForm.Meta):
        model = Worker

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            get_user_model()._default_manager.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user 

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = Worker


class ApiUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = MyUserChangeForm
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('money')}),
    )


admin.site.register(Image)
admin.site.register(Worker, ApiUserAdmin)
admin.site.register(Job)
admin.site.register(Crop)

# Register your models here.
