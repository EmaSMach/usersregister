from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import redirect


class UserLoginForm(forms.Form):
    """
    The login form.
    """
    username = forms.CharField()
    password = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                print user
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


User = get_user_model()


class RegisterForm(forms.ModelForm):
    """
    Register form.
    """
    username = forms.CharField()
    email = forms.EmailField(label="Email: ")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password:")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password:")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already being used")
        return redirect('profiles:simple_lst')
        #return super(RegisterForm, self).clean(*args, **kwargs)
