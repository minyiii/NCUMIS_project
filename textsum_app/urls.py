from django.urls import path
from . import views

# convert/
urlpatterns =[
    path('', views.upload, name='upload'), # POST/上傳.md檔
    # path('save/<int:id>/', views.json_save, name='json_save'), # POST/編輯頁面中儲存檔案(回傳JSON檔)
]