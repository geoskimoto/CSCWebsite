from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    status = forms.CharField(max_length=25)
    emergency_contact = forms.CharField(max_length=100)
    emergency_contact_phone = forms.IntegerField()

    class Meta:
        model = Member
        fields = ('email', 'name', 'username', 'status', 'emergency_contact', 'emergency_contact_phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.username = self.cleaned_data['username']
        user.status = self.cleaned_data['status']
        user.emergency_contact = self.cleaned_data['emergency_contact']
        user.emergency_contact_phone = self.cleaned_data['emergency_contact_phone']
        if commit:
            user.save()
        return user
