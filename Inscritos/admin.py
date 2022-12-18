from django.contrib import admin
from .models import Inscritos
# Register your models here.

class InscritoAdmin(admin.ModelAdmin):
    list_display=['nombre']
admin.site.register(Inscritos, InscritoAdmin)