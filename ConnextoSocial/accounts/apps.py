from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ConnextoSocial.accounts'

    def ready(self):
        import ConnextoSocial.accounts.signals

