from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
<<<<<<< HEAD
=======

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .models import MemberApplication, Member  # Adjust the import based on your project structure
# from validators import validate_email


from django.core.validators import EmailValidator
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

EMAIL_LIST = ['nick.steele.nv@gmail.com', 'geoskimoto@yahoo.com']

validate_email = EmailValidator(allowlist=EMAIL_LIST)
>>>>>>> origin/laptop

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Member  # Adjust the import based on your project structure
# from validators import validate_email


from django.core.validators import EmailValidator
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

EMAIL_LIST = ['nick.steele.nv@gmail.com', 'geoskimoto@yahoo.com']

validate_email = EmailValidator(allowlist=EMAIL_LIST)

class MembershipRegistrationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), validators=[validate_email])

<<<<<<< HEAD
    class Meta:
        model = Member
        fields = [
            'email', 'password1', 'password2',
            'phone_number',
            'emergency_contact', 'emergency_contact_phone',
            'is_family_member', 'is_employee', 'is_committee_member'
        ]
=======
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


from django.contrib.auth.forms import UserCreationForm
# should use the UserCreationFrom because it enforces unique users.
# UserCreationForm inherits BaseUserCreationFrom which has three fields: username (from the user model),
# password1, and password2. It verifies that password1 and password2 match, validates the password using
# validate_password(), and sets the user’s password using set_password().
# class MembershipRegistrationForm(UserCreationForm):
#     email = forms.EmailField(label=_("Email"), validators=[validate_email])
#
#     class Meta(UserCreationForm.Meta):
#         # fields = UserCreationForm.Meta.fields + ("email",)
#     # class Meta:
#         model = Member
#         fields = UserCreationForm.Meta.fields + (
#             # 'email', 'password1', 'password2',
#             'first_name', 'last_name', 'date_of_birth', 'occupation',
#             'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
#             'country', 'primary_phone', 'secondary_phone', 'website_url',
#             'joining_comments', 'emergency_contact', 'emergency_contact_phone',
#             'is_family_member', 'is_employee', 'is_committee_member'
#         )

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationWithEmailForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

from django import forms
from .models import Member

class MembershipRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            'first_name', 'last_name', 'date_of_birth', 'occupation',
            'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
            'country', 'primary_phone', 'secondary_phone', 'website_url',
            'joining_comments', 'emergency_contact', 'emergency_contact_phone',
            'is_family_member', 'is_employee', 'is_committee_member'
        )

class MembershipRegistrationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), validators=[validate_email])

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = (
            'email',  # Include email from User model
            'first_name', 'last_name', 'date_of_birth', 'occupation',
            'skills', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
            'country', 'primary_phone', 'secondary_phone', 'website_url',
            'joining_comments', 'emergency_contact', 'emergency_contact_phone',
            'is_family_member', 'is_employee', 'is_committee_member'
        )

    def save(self, commit=True):
        member = super().save(commit=False)
        member.email = self.cleaned_data['email']
        if commit:
            member.save()
        return member

    # password1 = forms.CharField(
    #     label=_("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput,
    #     help_text="Your password must contain at least 8 characters.",
    # )
    # password2 = forms.CharField(
    #     label=_("Password confirmation"),
    #     widget=forms.PasswordInput,
    #     strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
    # )
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             _("The two password fields didn't match."),
    #             code='password_mismatch',
    #         )
    #     return password2
    #
    # def save(self, commit=True):
    #     member = super().save(commit=False)
    #     password1 = self.cleaned_data["password1"]
    #     if password1:
    #         member.set_password(password1)
    #     if commit:
    #         member.save()
    #     return member
>>>>>>> origin/laptop

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