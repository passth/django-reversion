from django.apps import AppConfig


class ReversionConfig(AppConfig):
    name = 'reversion'
    default_auto_field = 'django.db.models.AutoField'

    def ready(self) -> None:
        from .conf import settings
        settings.load_from_settings()
