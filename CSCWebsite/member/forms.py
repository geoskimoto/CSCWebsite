from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import MemberApplication, Member  # Adjust the import based on your project structure
# from validators import validate_email


from django.core.validators import EmailValidator
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

EMAIL_LIST = ['nick.steele.nv@gmail.com', 'geoskimoto@yahoo.com']

validate_email = EmailValidator(allowlist=EMAIL_LIST)


class MembershipApplicationForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(MembershipApplicationForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = MemberApplication
        fields = [
            'first_name', 'last_name', 'email', 'date_of_birth', 'occupation',
            'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
            'country', 'phone_number', 'website_url',
            'joining_comments'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class MembershipRegistrationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), validators=[validate_email])

    class Meta:
        model = Member
        fields = [
            'email', 'password1', 'password2',
            'first_name', 'last_name', 'date_of_birth', 'occupation',
            'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
            'country', 'home_phone', 'work_phone', 'mobile_phone', 'website_url',
            'joining_comments', 'emergency_contact', 'emergency_contact_phone',
            'is_family_member', 'is_employee', 'is_committee_member'
        ]

User = get_user_model()
class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email or password.')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('This account is inactive.')
        return self.cleaned_data