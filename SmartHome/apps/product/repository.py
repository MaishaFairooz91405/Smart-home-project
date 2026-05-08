from product.models import Product


class ProductRepository():
    def create(self, data):
        return Product.objects.create(**data)
    def update(self, data):
        return Product.objects.get(pk=data['id'])
    def delete(self, data):
        return Product.objects.get(pk=data['id'])
    def list(self, data):
        return Product.objects.all()
    def detail(self, data):
        return Product.objects.get(pk=data['id'])