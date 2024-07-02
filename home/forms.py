from django import forms
from .models import MembershipApplication
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MembershipApplicationForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(MembershipApplicationForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = MembershipApplication
        fields = [
            'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'occupation',
            'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
            'country', 'home_phone', 'work_phone', 'mobile_phone', 'website_url',
            'joining_comments'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
