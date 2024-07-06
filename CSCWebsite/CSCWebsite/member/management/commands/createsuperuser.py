from django.contrib.auth.management.commands.createsuperuser import Command as BaseCreateSuperuserCommand
from django.core.management import CommandError


# class Command(BaseCreateSuperuserCommand):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def add_arguments(self, parser):
#         super().add_arguments(parser)
#         parser.add_argument('--date_of_birth', required=True, help='Date of birth')
#         parser.add_argument('--address_line_1', required=True, help='Address line 1')
#         parser.add_argument('--city', required=True, help='City')
#         parser.add_argument('--state', required=True, help='State')
#         parser.add_argument('--zip_code', required=True, help='Zip code')
#         parser.add_argument('--primary_phone', required=True, help='Primary phone')
#         parser.add_argument('--emergency_contact', required=True, help='Emergency contact')
#         parser.add_argument('--emergency_contact_phone', required=True, help='Emergency contact phone')
#
#     def handle(self, *args, **options):
#         date_of_birth = options.get('date_of_birth')
#         address_line_1 = options.get('address_line_1')
#         city = options.get('city')
#         state = options.get('state')
#         zip_code = options.get('zip_code')
#         primary_phone = options.get('primary_phone')
#         emergency_contact = options.get('emergency_contact')
#         emergency_contact_phone = options.get('emergency_contact_phone')
#
#         if not date_of_birth:
#             raise CommandError('Date of birth is required')
#         if not address_line_1:
#             raise CommandError('Address line 1 is required')


# from django.contrib.auth.management.commands.createsuperuser import Command as BaseCreateSuperuserCommand
# from django.core.management import CommandError

class Command(BaseCreateSuperuserCommand):
    help = 'Create a superuser with additional required fields'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--date_of_birth', required=True, help='Date of birth')
        parser.add_argument('--address_line_1', required=True, help='Address line 1')
        parser.add_argument('--city', required=True, help='City')
        parser.add_argument('--state', required=True, help='State')
        parser.add_argument('--zip_code', required=True, help='Zip code')
        parser.add_argument('--primary_phone', required=True, help='Primary phone')
        parser.add_argument('--emergency_contact', required=True, help='Emergency contact')
        parser.add_argument('--emergency_contact_phone', required=True, help='Emergency contact phone')

    def handle(self, *args, **options):
        date_of_birth = options.get('date_of_birth')
        address_line_1 = options.get('address_line_1')
        city = options.get('city')
        state = options.get('state')
        zip_code = options.get('zip_code')
        primary_phone = options.get('primary_phone')
        emergency_contact = options.get('emergency_contact')
        emergency_contact_phone = options.get('emergency_contact_phone')

        if not date_of_birth:
            raise CommandError('Date of birth is required')
        if not address_line_1:
            raise CommandError('Address line 1 is required')
        if not city:
            raise CommandError('City is required')
        if not state:
            raise CommandError('State is required')
        if not zip_code:
            raise CommandError('Zip code is required')
        if not primary_phone:
            raise CommandError('Primary phone is required')
        if not emergency_contact:
            raise CommandError('Emergency contact is required')
        if not emergency_contact_phone:
            raise CommandError('Emergency contact phone is required')

        super().handle(*args, **options)
