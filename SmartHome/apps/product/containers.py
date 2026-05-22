from dependency_injector import containers, providers

from .repository import ProductRepository
from .services import ProductService


class ProductContainer(containers.DeclarativeContainer):
    product_repo = providers.Singleton(ProductRepository)
    product_service = providers.Singleton(ProductService, product_repository=product_repo)
