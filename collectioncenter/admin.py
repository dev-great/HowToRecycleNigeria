from django.contrib import admin

from account.models import *
# Register your models here.


class CollectionCenterModelAdmin(admin.ModelAdmin):
    list_display = ['name','number','whats_app','state','google_map_link','full_address','opening_time','closing_time',]
    list_filter = ['state','opening_time','closing_time','pricing',]
    search_fields = ['name','number','whats_app','state','opening_time','closing_time','pricing',]
    
admin.site.register(CollectionCenterModel, CollectionCenterModelAdmin)