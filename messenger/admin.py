from django.contrib import admin
from . models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'timesent')
    list_per_page = 50
admin.site.register(Message,MessageAdmin)
