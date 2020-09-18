from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label="USERNAME:")
    password = forms.CharField(label="PASSWORD:",widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="PASSWORD:",widget = forms.PasswordInput(attrs  = {'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(label="CONFIRM PASSWORD",widget = forms.PasswordInput(attrs  = {'placeholder':'Confirm Password...'}))
    email = forms.EmailField(label='E-Mail')
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',

        )

    def clean_confirm_password(self):
         password = self.cleaned_data.get('password')
         confirm_password = self.cleaned_data.get('confirm_password')
         if password != confirm_password:
             raise forms.ValidationError("Password DO not match")
         return confirm_password
