from product.models import Product
from product.repository import ProductRepository


class ProductService:
    # is_generic = models.BooleanField(default=False)
    # is_deleted = models.BooleanField(default=False)
    product_repo = ProductRepository
    def create(self,request):
        return self.product_repo.create(request)



