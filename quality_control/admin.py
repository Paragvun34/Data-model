from django.contrib import admin
from .models import BugReport, FeatureRequest
# Register your models here.

@admin.register(BugReport)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'task', 'project')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)

    fieldsets = [
        (
            None,
            {
                "fields": ["title", "description", "status", "task"],
            },
        ),
        (
            "Advanced options",
            {
                "fields": ["priority", "created_at", 'updated_at'],
            },
        ),
    ]

    

@admin.register(FeatureRequest)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'task', 'project')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = [
        (
            None,
            {
                "fields": ["title", "description", "status", "task"],
            },
        ),
        (
            "Advanced options",
            {
                "fields": ["priority", "created_at", 'updated_at'],
            },
        ),
    ]