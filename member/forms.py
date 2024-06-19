from django import forms
from django.contrib.auth.forms import UsernameField
from .models import Member


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100)
    status = forms.CharField(max_length=25)
    emergency_contact = forms.CharField(max_length=100)
    emergency_contact_phone = forms.CharField(max_length=15)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('email', 'username', 'status', 'emergency_contact', 'emergency_contact_phone', 'password1', 'password2')
        field_classes = {'username': UsernameField}

    def clean_email(self):
        email = self.cleaned_data['email']
        if Member.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already registered.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
