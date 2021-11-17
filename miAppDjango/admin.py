from django.contrib import admin

# Register your models here.
from .models import Persona,Car

admin.site.register(Persona)
admin.site.register(Car)
