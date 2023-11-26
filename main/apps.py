from django.apps import AppConfig

class  MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        import main.signals  # Замість 'your_app_name' вкажіть назву вашого додатку