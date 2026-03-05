import os
import logging
from datetime import timedelta
from celery import shared_task

from django.utils import timezone

logger = logging.getLogger("delete_partial_upload")


def bytes_to_readable(num_bytes, suffix="B"):
    """Converts bytes to a human-readable format (e.g., KB, MB, GB)."""
    for unit in ["", "K", "M", "G", "T", "P"]:
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}{suffix}"
        num_bytes /= 1024


@shared_task(bind=True, max_retries=3, autoretry_for=(Exception,))
def delete_old_media_files(self, max_age_hours=24):

    from django.conf import settings
    from Logs.models import ExpiredChunkDeletionLog

    target_dir = os.path.join(
        settings.MEDIA_ROOT, settings.ADMIN_RESUMABLE_CHUNK_FOLDER
    )
    cutoff = timezone.now() - timedelta(hours=max_age_hours)
    cutoff_timestamp = cutoff.timestamp()

    if not os.path.isdir(target_dir):
        logger.error(f"Target directory does not exist: {target_dir}")
        return

    logger.info(
        f"Starting cleanup of '{target_dir}' — files older than {max_age_hours}h"
    )

    deleted, failed, skipped = [], [], []
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                mtime = os.path.getmtime(file_path)
                if mtime >= cutoff_timestamp:
                    skipped.append(file_path)
                    continue

                file_size_bytes = os.path.getsize(file_path)
                file_size = bytes_to_readable(file_size_bytes)
                file_age_hours = (timezone.now().timestamp() - mtime) / 3600
                logger.info(
                    f"Deleting: {file_path} "
                    f"(size={file_size}, age={file_age_hours:.1f}h)"
                )

                os.remove(file_path)
                ExpiredChunkDeletionLog.objects.create(
                    file_name=filename,
                    file_path=file_path,
                    file_size=file_size,
                    original_created_at=timezone.datetime.fromtimestamp(
                        mtime, tz=timezone.utc
                    ),
                    reason="age_policy",
                    success=True,
                )
                deleted.append(file_path)

            except Exception as e:
                logger.error(f"Failed to delete {file_path}: {e}")
                ExpiredChunkDeletionLog.objects.create(
                    file_name=filename,
                    file_path=file_path,
                    file_size=file_size,
                    original_created_at=timezone.datetime.fromtimestamp(
                        mtime, tz=timezone.utc
                    ),
                    reason="age_policy",
                    success=False,
                    error_message=str(e),
                )
                failed.append(file_path)

    logger.info(
        f"Cleanup complete — deleted: {len(deleted)}, failed: {len(failed)}, skipped (too new): {len(skipped)}"
    )
    return {
        "deleted": len(deleted),
        "failed": len(failed),
        "skipped": len(skipped),
        "completed_at": timezone.now().isoformat(),
    }
