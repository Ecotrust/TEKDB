from django import template
import psutil


register = template.Library()


def disk_space_percent():
    """Returns the percentage of used disk space."""
    usage = psutil.disk_usage("/")
    return usage.percent


def disk_space_free():
    """Returns the free disk space in GB or MB"""
    usage = psutil.disk_usage("/")
    free_disk_space_gb = usage.free // (2**30)  # Convert bytes to GB
    if free_disk_space_gb < 1:
        return f"{usage.free // (2**20)} MB"  # Convert bytes to MB
    return f"{free_disk_space_gb} GB"


def disk_space_used():
    """Returns the used disk space in GB or MB"""
    usage = psutil.disk_usage("/")
    used_disk_space_gb = usage.used // (2**30)  # Convert bytes to GB
    if used_disk_space_gb < 1:
        return f"{usage.used // (2**20)} MB"  # Convert bytes to MB
    return f"{used_disk_space_gb} GB"


def memory_usage_percent():
    """Returns the percentage of used memory"""
    memory = psutil.virtual_memory()
    return memory.percent


def memory_free():
    """Returns the free memory in GB or MB"""
    memory = psutil.virtual_memory()
    free_memory_gb = memory.available // (2**30)  # Convert bytes to GB
    if free_memory_gb < 1:
        return f"{memory.available // (2**20)} MB"  # Convert bytes to MB
    return f"{free_memory_gb} GB"


def memory_used():
    """Returns the used memory"""
    memory = psutil.virtual_memory()
    used_memory_gb = memory.used // (2**30)  # Convert bytes to GB
    if used_memory_gb < 1:
        return f"{memory.used // (2**20)} MB"  # Convert bytes to MB
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
