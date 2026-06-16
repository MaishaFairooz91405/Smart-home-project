from .models import Inventory
from common.constants import PRODUCT_NOT_FOUND


def get_inventory_products(*, is_deleted=None):
    queryset = Inventory.objects.all().order_by('id')

    if is_deleted is not None:
        queryset = queryset.filter(is_deleted=is_deleted)
    return queryset

def get_inventory_product_by_id(inventory_id):
    inventory_product= Inventory.objects.get(id=inventory_id)
    if not inventory_product or inventory_product.is_deleted:
        raise Exception(PRODUCT_NOT_FOUND)
    return inventory_product