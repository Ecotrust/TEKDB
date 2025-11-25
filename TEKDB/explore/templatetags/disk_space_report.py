from django import template
import psutil


register = template.Library()


def bytes_to_mb(bytes_value):
    """Converts bytes to MB."""
    return bytes_value >> 20


def bytes_to_gb(bytes_value):
    """Converts bytes to GB."""
    return bytes_value >> 30


def disk_space_percent():
    """Returns the percentage of used disk space."""
    usage = psutil.disk_usage("/")
    return usage.percent


def disk_space_free():
    """Returns the free disk space in GB or MB"""
    usage = psutil.disk_usage("/")
    free_disk_space_gb = bytes_to_gb(usage.free)
    if free_disk_space_gb < 1:
        return f"{bytes_to_mb(usage.free)} MB"
    return f"{free_disk_space_gb} GB"


def disk_space_used():
    """Returns the used disk space in GB or MB"""
    usage = psutil.disk_usage("/")
    used_disk_space_gb = bytes_to_gb(usage.used)
    if used_disk_space_gb < 1:
        return f"{bytes_to_mb(usage.used)} MB"
    return f"{used_disk_space_gb} GB"


def memory_usage_percent():
    """Returns the percentage of used memory"""
    memory = psutil.virtual_memory()
    return memory.percent


def memory_free():
    """Returns the free memory in GB or MB"""
    memory = psutil.virtual_memory()
    free_memory_gb = bytes_to_gb(memory.available)
    if free_memory_gb < 1:
        return f"{bytes_to_mb(memory.available)} MB"
    return f"{free_memory_gb} GB"


def memory_used():
    """Returns the used memory in GB or MB"""
    memory = psutil.virtual_memory()
    used_memory_gb = bytes_to_gb(memory.used)
    if used_memory_gb < 1:
        return f"{bytes_to_mb(memory.used)} MB"
    return f"{used_memory_gb} GB"


@register.simple_tag(name="disk_space_report")
def disk_space_report():
    """Returns a dictionary with disk space and memory usage information."""
    return {
        "disk_space_free": disk_space_free(),
        "disk_space_used_percent": disk_space_percent(),
        "disk_space_used": disk_space_used(),
        "memory_free": memory_free(),
        "memory_used": memory_used(),
        "memory_used_percent": memory_usage_percent(),
    }
