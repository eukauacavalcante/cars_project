from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
    verbose_name = 'Carros'

    def ready(self):
        import cars.signals
