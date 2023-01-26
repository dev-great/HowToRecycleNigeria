from django.contrib import admin
from .models import *

# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name','details',)
#     search_fields = ['name','details',]
    
# admin.site.register(ServiceModel, ServiceAdmin)

admin.site.register(BlogModel)
admin.site.register(NewslettersModel)
admin.site.register(ContaclFormModel)