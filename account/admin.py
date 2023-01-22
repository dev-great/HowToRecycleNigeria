from django.contrib import admin
from .models import *
# Register your models here.


class BecomeAnAgentAdmin(admin.ModelAdmin):
    list_display = ('name','phoneNumber','state','status',)
    list_filter = ('state','status',)
    search_fields = ['name','phoneNumber','state','status',]
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(BecomeAnAgent, BecomeAnAgentAdmin)