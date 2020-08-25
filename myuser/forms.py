from django import forms
from myuser.models import MyUser

class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["username", "password", "display_name", "age", "homepage"]
        widgets = {'password': forms.PasswordInput()}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)