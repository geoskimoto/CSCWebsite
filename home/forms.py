from django import forms
from .models import MembershipApplication

class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = [
            'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'occupation',
            'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
            'country', 'home_phone', 'work_phone', 'mobile_phone', 'fax', 'website_url',
            'joining_comments'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
