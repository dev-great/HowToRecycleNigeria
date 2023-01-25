from django.contrib import admin

from account.models import *
# Register your models here.


class BecomeAnAgentAdmin(admin.ModelAdmin):
    list_display = ('name','phoneNumber','state','email',)
    list_filter = ('state',)
    search_fields = ['name','phoneNumber','state','email',]
    
admin.site.register(BecomeAnAgent, BecomeAnAgentAdmin)