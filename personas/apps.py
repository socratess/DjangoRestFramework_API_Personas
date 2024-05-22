from django.apps import AppConfig
from django.core.management import call_command


class PersonasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "personas"

    def ready(self):
        call_command('data')