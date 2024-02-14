from django.contrib import admin
from todo.models import Task


@admin.register(Task)
class AdminModels(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'user']
    list_display_links = ['title', 'user']
    search_fields = ['title', 'user']
    list_filter = ['user']
