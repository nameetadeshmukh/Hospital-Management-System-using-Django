from django.contrib import admin
from .models import Patient, Doctor, Appointment

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
  list_display=['Name','mobile','special']
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient)
admin.site.register(Appointment)
