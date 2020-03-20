from django.contrib import admin
from .models import Doctor,Chemist,LabChemist
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Chemist)
admin.site.register(LabChemist)