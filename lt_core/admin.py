from django.contrib import admin

from lt_core.models import UserState, Topic, Record
# Register your models here.

admin.site.register(UserState)
admin.site.register(Topic)
admin.site.register(Record)
