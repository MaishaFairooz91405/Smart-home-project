from django.shortcuts import get_object_or_404
from utilis.filter import get_filters
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

    def get(self, filters):
        return Product.objects.filter(**filters)

    def get_by_id(self, filters):
        return Product.objects.filter(**filters).first()
