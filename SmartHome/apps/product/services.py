from product.repository import ProductRepository

class ProductService:

    def __init__(self, product_repository):
        self.product_repository = product_repository

    def create_product(self, data):
        return self.product_repository.create(data)

    def update_product(self, data):
        return self.product_repository.update(data)

    def delete_product(self, data):
        return self.product_repository.delete(data)

    def get_products(self, is_generic=None, is_deleted=None):

        queryset = self.product_repository.list()

        if is_generic is not None:
            queryset = self.product_repository.filter_by_generic(is_generic)

        if is_deleted is not None:
            queryset = self.product_repository.filter_by_deleted(is_deleted)

        return queryset


    def get_product_detail(self, data):
        return self.product_repository.detail(data)
