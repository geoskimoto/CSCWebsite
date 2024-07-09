from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
# from .models import MemberApplication, Member  # Adjust the import based on your project structure
# from validators import validate_email
from django.contrib.auth import get_user_model
# from .models import Reservation, Bunk


from django.core.validators import EmailValidator
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# EMAIL_LIST = ['nick.steele.nv@gmail.com', 'geoskimoto@yahoo.com']
#
# validate_email = EmailValidator(allowlist=EMAIL_LIST)


from django import forms
from .models import Bunk, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['bunk', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'check_out': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError("Check-out time must be after check-in time.")

        return cleaned_data


# class MembershipApplicationForm(forms.ModelForm):
#     # def __init__(self, *args, **kwargs):
#     #     super(MembershipApplicationForm, self).__init__(*args, **kwargs)
#     #     self.helper = FormHelper()
#     #     self.helper.form_method = 'post'
#     #     self.helper.add_input(Submit('submit', 'Submit'))
#     class Meta:
#         model = MemberApplication
#         fields = [
#             'first_name', 'last_name', 'email', 'date_of_birth', 'occupation',
#             'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
#             'country', 'primary_phone', 'secondary_phone', 'website_url',
#             'joining_comments'
#         ]
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
#         }
#
#
# class MembershipRegistrationForm(UserCreationForm):
#     email = forms.EmailField(label=_("Email"), validators=[validate_email])
#
#     class Meta:
#         model = Member
#         fields = [
#             'email', 'password1', 'password2',
#             'first_name', 'last_name', 'date_of_birth', 'occupation',
#             'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
#             'country', 'primary_phone', 'secondary_phone', 'website_url',
#             'joining_comments', 'emergency_contact', 'emergency_contact_phone',
#             'is_family_member', 'is_employee', 'is_committee_member'
#         ]
#
# User = get_user_model()
# class EmailAuthenticationForm(AuthenticationForm):
#     email = forms.EmailField(label='Email')
#
#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         if email and password:
#             self.user_cache = authenticate(self.request, email=email, password=password)
#             if self.user_cache is None:
#                 raise forms.ValidationError('Invalid email or password.')
#             elif not self.user_cache.is_active:
#                 raise forms.ValidationError('This account is inactive.')
#         return self.cleaned_data