from django.contrib import admin
from inventory.models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'room',
        'quantity',
        'created_by',
        'updated_by',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'title',
        'room_id',
    ]

    list_filter = [
        'title',
        'room_id',
        'created_by',
        'updated_by',
        'is_deleted'
    ]

    ordering = ['id']

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    def has_add_permission(self, request):
        return True # change to False if you want to block adding

    def has_delete_permission(self, request, obj=None):
        return False  # prevents deletion


admin.site.register(Inventory, InventoryAdmin)
# Register your models here.
