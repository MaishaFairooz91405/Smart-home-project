from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

    def ready(self):
        from .containers import ProductContainer
        container = ProductContainer()
        container.init_resources()
        self.container = container
