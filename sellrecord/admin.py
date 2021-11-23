from django.contrib import admin
from .models import Sellrecord
# Register your models here.
admin.site.register(Sellrecord)

class SellrecordAdmin(admin.modelAdmin):
    list_display= ['customer_name', 'customer_phone']

admin.site register(Sellrecord, SellrecordAdmin)