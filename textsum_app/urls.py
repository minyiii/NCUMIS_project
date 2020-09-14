from django.urls import path
from . import views

# convert/
urlpatterns =[
    path('', views.upload, name='upload'), # POST/上傳.md檔
]