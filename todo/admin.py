from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',) #this line shows up the uneditable field 'created' of the Todo model IN THE ADMIN PANEL. However, this is 'read-only' and cannot be edited.

admin.site.register(Todo,TodoAdmin)