from django.contrib import admin
from .models import ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_by',
        'updated_by',
        'created_at',
        'is_deleted'
    ]

    search_fields = [
        'title',
    ]

    list_filter = [
        'is_deleted',
        'created_at'
    ]

    ordering = ['created_at']

    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    # ✅ 8. Disable add (optional)
    def has_add_permission(self, request):
        return True  # change to False if you want to block adding

    # ✅ 9. Disable delete (optional)
    def has_delete_permission(self, request, obj=None):
        return False  # prevents deletion


# ✅ Register model
admin.site.register(ProductCategory, ProductCategoryAdmin)
