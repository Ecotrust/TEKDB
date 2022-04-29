from django.contrib import admin

# Register your models here.
from configuration.models import Configuration

admin.site.register(Configuration)