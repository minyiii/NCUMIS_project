from django.urls import path
from . import views
# from django.views.generic.base import View

# mindmap/
urlpatterns =[
    path('', views.get_mindmap, name='get_mindmap'), # 取得此用戶的所有心智圖
    path('edit/<int:id>/', views.edit_mindmap, name='edit_mindmap'), # 開啟某一心智圖
    path('edit/<int:id>/save', views.save_json, name='save_json'), # *儲存檔案，前端傳json檔來
    path('delete/<int:id>/', views.del_mindmap, name='del_mindmap'), # 刪除某一心智圖
    path('edit_des/<int:id>/', views.edit_describe, name='edit_describe'), # *編輯某一心智圖的敘述
]