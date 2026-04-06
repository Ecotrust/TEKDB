import shutil


def bytes_to_readable(num_bytes, suffix="B"):
    """Converts bytes to a human-readable format (e.g., KB, MB, GB)."""
    for unit in ["", "K", "M", "G", "T", "P"]:
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}{suffix}"
        num_bytes /= 1024


def check_disk_space(required_bytes, path="/"):
    """Return (has_space, free_bytes) for the filesystem containing `path`."""
    disk = shutil.disk_usage(path)
    return disk.free >= required_bytes, disk.free
