from product.repository import ProductRepository
from product.services import ProductService


class ProductContainer:

    @staticmethod
    def product_service():
        repository = ProductRepository()

        return ProductService(repository)
