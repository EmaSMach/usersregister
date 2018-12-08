from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class UserLoginForm(forms.Form):
#     """
#     The login form.
#     """
#     username = forms.CharField()
#     password = forms.CharField()
#
#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user is None:
#                 print user
#                 raise forms.ValidationError("This user does not exist")
#             if not user.check_password(password):
#                 raise forms.ValidationError("Incorrect Password")
#             if not user.is_active:
#                 raise forms.ValidationError("This user is not active")
#         return super(UserLoginForm, self).clean(*args, **kwargs)


class SignUpForm(UserCreationForm):
    """
    Extends the UserCreationForm to add an email field.
    """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')
