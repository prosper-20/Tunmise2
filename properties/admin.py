from django.contrib import admin
from .models import Properties

@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "status"]
    list_filter = ["type", "status"]



# admin.site.register(Properties, PropertiesAdmin)
