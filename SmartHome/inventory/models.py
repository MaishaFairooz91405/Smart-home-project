from django.db import models
from django.core.exceptions import ValidationError
from product.models import ProductCategory
from room.models import Room
from django.contrib.auth.models import User
# from .managers import InventoryManager


class Inventory(models.Model):
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="inventory_items"
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    quantity = models.IntegerField(default=0)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="inventories_created"
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="inventories_updated"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, null=False)


    def __str__(self):
        return self.title

    class Meta:
        db_table = "inventory"
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"

    


