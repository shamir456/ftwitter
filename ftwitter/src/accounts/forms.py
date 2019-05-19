from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    pass1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    pass2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    def clean_password2(self):
        pass1 = self.cleaned_data.get('pass1')
        pass2 = self.cleaned_data.get('pass2')
        if pass1 != pass2:
            raise forms.ValidationError("Password must match")
        return pass1

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("This username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError(" Email is already registered.") 
        if not email.endswith('@nu.edu.pk'):
            raise forms.ValidationError("Only nu.edu.pk email addresses allowed")
        return email
