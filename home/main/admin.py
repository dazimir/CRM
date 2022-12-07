from django.contrib import admin

# Register your models here.
from .models import Task, Card, Taskobj

admin.site.register(Task)
admin.site.register(Card)
admin.site.register(Taskobj)
