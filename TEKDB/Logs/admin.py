from django.contrib import admin
from Logs.models import ExpiredChunkDeletionLog


class ExpiredChunkDeletionLogAdmin(admin.ModelAdmin):
    readonly_fields = [
        "file_name",
        "file_path",
        "file_size",
        "original_created_at",
        "deleted_at",
        "reason",
        "success",
        "error_message",
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ExpiredChunkDeletionLog, ExpiredChunkDeletionLogAdmin)
