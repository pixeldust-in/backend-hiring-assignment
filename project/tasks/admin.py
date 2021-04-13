from django.contrib import admin

from tasks.models import Project, Task

admin.site.register(Project)
admin.site.register(Task)