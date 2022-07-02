from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["todo_text"]}),
        ("Date Info", {"fields": ["create_date"], "classes": ["collapse"]}),
    ]


admin.site.register(Todo, TodoAdmin)
