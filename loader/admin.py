from django.contrib import admin
from .models import Content, About

class ContentAdmin(admin.ModelAdmin):
    list_display = ('page', 'title', 'image', 'info')
    
#class AboutAdmin(admin.ModelAdmin):
#    list_display = ('title', 'description')    
# Register your models here.
admin.site.register(Content, ContentAdmin)
#admin.site.register(About, AboutAdmin)


