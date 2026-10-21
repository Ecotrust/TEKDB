from django.test import TestCase
from unittest.mock import patch
import shutil

from TEKDB.utils import bytes_to_readable, check_disk_space


class TestBytesToReadable(TestCase):
    def test_bytes(self):
        self.assertEqual(bytes_to_readable(512), "512.00 B")

    def test_kilobytes(self):
        self.assertEqual(bytes_to_readable(1024), "1.00 KB")
        self.assertEqual(bytes_to_readable(2048), "2.00 KB")

    def test_megabytes(self):
        self.assertEqual(bytes_to_readable(1024 * 1024), "1.00 MB")
        self.assertEqual(bytes_to_readable(5.5 * 1024 * 1024), "5.50 MB")

    def test_gigabytes(self):
        self.assertEqual(bytes_to_readable(1024 * 1024 * 1024), "1.00 GB")

    def test_terabytes(self):
        self.assertEqual(bytes_to_readable(1024 * 1024 * 1024 * 1024), "1.00 TB")

    def test_petabytes(self):
        self.assertEqual(bytes_to_readable(1024 * 1024 * 1024 * 1024 * 1024), "1.00 PB")

    def test_1026_petabytes(self):
        self.assertEqual(
            bytes_to_readable(1026 * 1024 * 1024 * 1024 * 1024 * 1024), "1026.00 PB"
        )

    def test_zero_bytes(self):
        self.assertEqual(bytes_to_readable(0), "0.00 B")

    def test_custom_suffix(self):
        self.assertEqual(bytes_to_readable(512, suffix="iB"), "512.00 iB")
        self.assertEqual(bytes_to_readable(1024, suffix="iB"), "1.00 KiB")


class TestCheckDiskSpace(TestCase):
    def test_sufficient_space(self):
        with patch("shutil.disk_usage") as mock_disk_usage:
            mock_disk_usage.return_value = shutil._ntuple_diskusage(
                free=1024 * 1024 * 1024,
                total=10 * 1024 * 1024 * 1024,
                used=9 * 1024 * 1024 * 1024,
            )
            has_space, free_bytes = check_disk_space(512 * 1024 * 1024)
            self.assertTrue(has_space)
            self.assertEqual(free_bytes, 1024 * 1024 * 1024)

    def test_insufficient_space(self):
        with patch("shutil.disk_usage") as mock_disk_usage:
            mock_disk_usage.return_value = shutil._ntuple_diskusage(
                free=256 * 1024 * 1024,
                total=10 * 1024 * 1024 * 1024,
                used=9 * 1024 * 1024 * 1024,
            )
            has_space, free_bytes = check_disk_space(512 * 1024 * 1024)
            self.assertFalse(has_space)
            self.assertEqual(free_bytes, 256 * 1024 * 1024)

    def test_exact_space(self):
        with patch("shutil.disk_usage") as mock_disk_usage:
            mock_disk_usage.return_value = shutil._ntuple_diskusage(
                free=512 * 1024 * 1024,
                total=10 * 1024 * 1024 * 1024,
                used=9 * 1024 * 1024 * 1024,
            )
            has_space, free_bytes = check_disk_space(512 * 1024 * 1024)
            self.assertTrue(has_space)
            self.assertEqual(free_bytes, 512 * 1024 * 1024)

    def test_custom_path(self):
        with patch("shutil.disk_usage") as mock_disk_usage:
            mock_disk_usage.return_value = shutil._ntuple_diskusage(
                free=1024, total=10 * 1024 * 1024 * 1024, used=9 * 1024 * 1024 * 1024
            )
            check_disk_space(512, path="/tmp")
            mock_disk_usage.assert_called_once_with("/tmp")
