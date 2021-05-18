from django.contrib import admin
from .models import Package
from .models import Sort_data
from .models import Alarm

admin.site.register(Package)
admin.site.register(Sort_data)
admin.site.register(Alarm)