from django.contrib import admin

from .models import *

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'finished')

admin.site.register(TaskModel, TaskAdmin)