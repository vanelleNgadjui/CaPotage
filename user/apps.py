from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        try:
            import app.signals  # noqa F401
        except ImportError:
            pass
