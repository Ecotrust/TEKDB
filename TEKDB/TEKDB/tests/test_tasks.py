import os
import time
from django.test import TestCase, override_settings

from TEKDB.tasks import delete_expired_chunks


class DeleteExpiredChunksTest(TestCase):
    def test_missing_dir_returns_none(self):
        with override_settings(
            MEDIA_ROOT="/nonexistent", ADMIN_RESUMABLE_CHUNK_FOLDER="does_not_exist"
        ):
            result = delete_expired_chunks.run(max_age_hours=24)
        self.assertIsNone(result)

    def test_deletes_expired_chunks_and_skips_new(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp_path:
            target = os.path.join(tmp_path, "chunks")
            os.makedirs(target)

            old_file = os.path.join(target, "old.bin")
            new_file = os.path.join(target, "new.bin")
            with open(old_file, "wb") as f:
                f.write(b"old")
            with open(new_file, "wb") as f:
                f.write(b"new")

            now = time.time()
            os.utime(old_file, (now - 48 * 3600, now - 48 * 3600))  # 48 hours old
            os.utime(new_file, (now - 1 * 3600, now - 1 * 3600))  # 1 hour old

            with override_settings(
                MEDIA_ROOT=tmp_path, ADMIN_RESUMABLE_CHUNK_FOLDER="chunks"
            ):
                result = delete_expired_chunks.run(max_age_hours=24)

            self.assertIsInstance(result, dict)
            self.assertEqual(result["deleted"], 1)
            self.assertEqual(result["skipped"], 1)
            self.assertEqual(result["failed"], 0)
            self.assertFalse(os.path.exists(old_file))
            self.assertTrue(os.path.exists(new_file))
