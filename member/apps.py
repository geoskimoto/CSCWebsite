from django.apps import AppConfig
# from . import signals  #this is causing a "AppRegistryNotReady" error.  Turning it off for now.

# class BookConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'member'


class MemberConfig(AppConfig):
    name = 'member'  # This is actually pretty crucial.  Make sure it's the same name as the directory.  Then you can import
    # files or models from this app into others by "from member.models import Members".

    # def ready(self):
    #     import signals