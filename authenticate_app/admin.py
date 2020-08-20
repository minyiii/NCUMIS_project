from django.contrib import admin
from .models import jsonContent 
# Register your models here.


# 預設資料庫內容管理介面
class JsonContentAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content') 
    fields = ('author', 'title', 'content') 
    search_fields = ['title']    
    list_filter = ['author']   
 


admin.site.register(jsonContent, JsonContentAdmin)  