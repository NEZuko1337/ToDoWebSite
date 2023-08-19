from django.contrib import admin
from . models import *

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'date',              
    )

admin.site.register(Todo, TodoAdmin)
