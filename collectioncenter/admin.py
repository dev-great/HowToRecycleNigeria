from django.contrib import admin

from account.models import *
# Register your models here.


class CollectionCenterModelAdmin(admin.ModelAdmin):
    list_display = ['name','number','whats_app','state','full_address','opening_time','closing_time',]
    list_filter = ['state','opening_time','closing_time',]
    search_fields = ['name','number','whats_app','state','opening_time','closing_time',]
    
admin.site.register(CollectionCenterModel, CollectionCenterModelAdmin)