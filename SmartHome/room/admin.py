from django.contrib import admin
from room.models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'created_by',
        'updated_by',
        'created_at',
        'updated_at',
        'is_deleted'
    ]
    search_fields = [
        'title',
    ]

    list_filter = [
        'title',
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
        return True  # change to False if you want to block adding

    def has_delete_permission(self, request, obj=None):
        return False  # prevents deletion


admin.site.register(Room, RoomAdmin)
# Register your models here.
from django.contrib import admin

# Register your models here.
