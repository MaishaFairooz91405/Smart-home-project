from django.contrib import admin
from .models import ProductCategory
from .models import Product

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
    ]
    ordering = ['created_at']

    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    def has_add_permission(self, request):
        return True  # change to False if you want to block adding

    def has_delete_permission(self, request, obj=None):
        return False  # prevents deletion

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'created_by',
        'updated_by',
        'created_at',
        'is_generic',
        'is_deleted'
    ]
    search_fields = [
        'title',
    ]
    list_filter = [
        'is_generic',
        'created_by',
        'updated_by'
    ]
    ordering = ['id']
    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    def has_add_permission(self, request):
        return True  # change to False if you want to block adding

    def has_delete_permission(self, request, obj=None):
        return False  # prevents deletion
admin.site.register(Product, ProductAdmin)