from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from menu.models import Menu


admin.site.register(Menu, DraggableMPTTAdmin)