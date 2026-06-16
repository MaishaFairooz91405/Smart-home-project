import django_filters
from .models import Inventory


class InventoryFilter(django_filters.FilterSet):
    min_quantity = django_filters.NumberFilter(field_name="quantity", lookup_expr="gte")
    max_quantity = django_filters.NumberFilter(field_name="quantity", lookup_expr="lte")

    class Meta:
        model = Inventory
        fields = ["product_category", "min_quantity", "max_quantity"]
