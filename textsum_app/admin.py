from django.contrib import admin
from textsum_app.models import jsonContent

# 預設資料庫內容管理介面
class JsonContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'upload', 'content')
    fields = ('author', 'title', 'upload','content')
    ordering = ['id']
    search_fields = ['title']
    list_filter = ['author']

admin.site.register(jsonContent, JsonContentAdmin)