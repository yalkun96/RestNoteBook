from django.apps import AppConfig



class RestbookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restbook'

    def ready(self):
        import restbook.signals