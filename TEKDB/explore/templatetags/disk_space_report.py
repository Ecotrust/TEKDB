from django import template
import psutil


register = template.Library()


def bytes_to_readable(num_bytes, suffix="B"):
    """Converts bytes to a human-readable format (e.g., KB, MB, GB)."""
    for unit in ["", "K", "M", "G", "T", "P"]:
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}{suffix}"
        num_bytes /= 1024


@register.simple_tag(name="disk_space_report")
def disk_space_report():
    """Returns a dictionary with disk space and memory usage information."""
    try:
        memory = psutil.virtual_memory()
        disk_usage = psutil.disk_usage("/")
        return {
            "disk_space_free": bytes_to_readable(disk_usage.free),
            "disk_space_used_percent": disk_usage.percent,
            "disk_space_used": bytes_to_readable(disk_usage.used),
            "memory_free": bytes_to_readable(memory.available),
            "memory_used": bytes_to_readable(memory.used),
            "memory_used_percent": memory.percent,
        }
    except Exception:
        return {
            "disk_space_free": "N/A",
            "disk_space_used_percent": "N/A",
            "disk_space_used": "N/A",
            "memory_free": "N/A",
            "memory_used": "N/A",
            "memory_used_percent": "N/A",
        }
