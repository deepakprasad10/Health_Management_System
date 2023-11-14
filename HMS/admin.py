from django.contrib import admin
from HMS.models import Appointment

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','mobileno']

