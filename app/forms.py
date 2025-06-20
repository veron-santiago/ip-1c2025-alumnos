from django import forms


class RegisterForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()