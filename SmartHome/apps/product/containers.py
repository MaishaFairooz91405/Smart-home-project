from .repository import ProductRepository
from .services import ProductService


class ProductContainer:

    @staticmethod
    def product_service():
        repository = ProductRepository()

        return ProductService(repository)
