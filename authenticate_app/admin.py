from django.contrib import admin
from .models import jsonContent 
# Register your models here.



class JsonContentAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'upload', 'content') 
    fields = ('author', 'title', 'upload','content') 
    search_fields = ['title']    
    list_filter = ['author']   
 


admin.site.register(jsonContent, JsonContentAdmin)  