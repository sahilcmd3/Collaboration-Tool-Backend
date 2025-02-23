from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, Document, Message, Task, Role, File

admin.site.register(CustomUser)
admin.site.register(Document)
admin.site.register(Message)
admin.site.register(Task)
admin.site.register(Role)
admin.site.register(File)