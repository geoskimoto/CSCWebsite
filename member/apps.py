from django.apps import AppConfig
# from . import signals  #this is causing a "AppRegistryNotReady" error.  Turning it off for now.

# class BookConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'member'


class MemberConfig(AppConfig):
    name = 'member'

    # def ready(self):
    #     import signals