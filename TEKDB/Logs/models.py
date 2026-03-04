from django.db import models


class ExpiredChunkDeletionLog(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    file_size = models.CharField(max_length=50, null=True)
    original_created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=100, default="age_policy")
    success = models.BooleanField(default=True)
    error_message = models.TextField(blank=True)

    class Meta:
        indexes = [models.Index(fields=["deleted_at"])]
        verbose_name = "Partial Upload Deletion Log"
        verbose_name_plural = "Partial Upload Deletion Logs"
