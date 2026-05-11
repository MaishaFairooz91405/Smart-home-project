from apps.product.models import Product


class ProductRepository:

    def create(self, data):
        return Product.objects.create(**data)

    def update(self, data):
        product = Product.objects.get(pk=data['id'])
        product.title = data.get('title', product.title)
        product.description = data.get('description', product.description)
        product.save()
        return product

    def delete(self, data):
        product = Product.objects.get(pk=data['id'])
        product.delete()
        return True

    def list(self):
        return Product.objects.all()
    def filter_by_generic(self,is_generic):
        return Product.objects.filter(is_generic=is_generic)
    def filter_by_deleted(self,is_deleted):
        return Product.objects.filter(is_deleted=is_deleted)


    def detail(self, data):
        return Product.objects.get(pk=data['id'])
