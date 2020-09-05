from django.urls import path
from . import views


urlpatterns =[
    path('convert/', views.convert, name='convert'), # 轉換區
    path('mmedit/<int:mmid>/', views.mmedit, name='mmedit'), # 編輯心智圖
    # path('mmedit/<int:mmid>/', views.mmedit2, name='mmedit'), # 編輯心智圖
    path('mindmap/', views.mindmap, name='mindmap'), # 筆記區
    # path('mmedit/<int:mmid>/', views.update_json, name='update_json'), # 更新筆記
    # path('mindmap/<int:del_id>/', views.delete, name='delete_mm'), # 刪除筆記
]