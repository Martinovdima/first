from django.contrib import admin
from .models import Package
from .models import Alarm

admin.site.register(Package)
admin.site.register(Alarm)