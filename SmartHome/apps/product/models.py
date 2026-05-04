from django.db import models
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_categories",
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="updated_categories",
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product_category"
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
