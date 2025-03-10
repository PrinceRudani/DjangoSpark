from django.apps import AppConfig


class SubcategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subcategory'

    def ready(self):
        import subcategory.signals  # Import signals when the app is ready