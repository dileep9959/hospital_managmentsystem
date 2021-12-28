from django.contrib import admin
from.models import appointment, docter,patient

# Register your models here.
admin.site.register(docter)
admin.site.register(patient)
admin.site.register(appointment)
