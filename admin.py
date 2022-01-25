from django.contrib import admin

from .models import Task, TaskUpdate

# Register your models here.

class UpdateInline(admin.TabularInline):
    model = TaskUpdate
    readonly_fields = ["old_status", "new_status", "time"]
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = [
        "title",
        "status",
    ]
    inlines = [UpdateInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskUpdate)
