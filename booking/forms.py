from django import forms
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from .models import Reservation, Bunk


class BunkReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['bunk', 'start_date', 'end_date']
        labels = {
            'bunk': 'Select Bunk',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bunk'].queryset = Bunk.objects.filter(assigned_to=self.current_user)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.member = self.current_user
        if commit:
            instance.save()
        return instance

    @property
    def current_user(self):
        return get_user_model().objects.get(pk=self.request.user.pk)
=======
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


from django.shortcuts import render, HttpResponse
from .models import Bunk, Booking
# from utils.booking_funcs import check_availability, get_user_bookings, get_all_bunks

class AvailabilityForm(forms.ModelForm):
    pass
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['bunk', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
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
>>>>>>> origin/laptop
