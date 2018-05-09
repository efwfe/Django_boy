from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name = "Users"

    def ready(self):

        try:
            import users.signals
        except ImportError:
            pass