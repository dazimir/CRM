from django.contrib import admin

# Register your models here.
from .models import Task, Card

admin.site.register(Task)
admin.site.register(Card)