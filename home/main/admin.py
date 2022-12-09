from django.contrib import admin
from .models import Task, Card, Taskobj, IndividualCustomer, OrganizationCustomer, Auntifications, Region

admin.site.register(Task)
admin.site.register(Card)
admin.site.register(Taskobj)
admin.site.register(IndividualCustomer)
admin.site.register(OrganizationCustomer)
admin.site.register(Auntifications)
admin.site.register(Region)
