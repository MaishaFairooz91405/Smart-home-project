from product.models import Product


class ProductRepository:

    def create(self, data):
        return Product.objects.create(**data)

    def get_by_id(self, product_id):
        return Product.objects.get(pk=product_id)

    def update(self, instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, product):
        product.delete()
        return True

    def soft_delete(self, product):
        product.is_deleted = True
        product.save(update_fields=["is_deleted"])
        return product

    def get(self, filters):
        return Product.objects.filter(**filters).order_by('id')
