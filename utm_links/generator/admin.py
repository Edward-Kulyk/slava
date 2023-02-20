from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UtmLink
from .models import ShortIO

admin.site.register(UtmLink)
admin.site.register(ShortIO)
