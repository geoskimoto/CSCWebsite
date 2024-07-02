from django.core.validators import EmailValidator
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

EMAIL_LIST = ['nick.steele.nv@gmail.com', 'geoskimoto@yahoo.com']

validate_email = EmailValidator(allowlist=EMAIL_LIST)