from django.urls import path
from . import views


urlpatterns =[
    path('convert/',views.convert,name='convert'),
    # path('home/',views.home,name='welcome'),
    # path('logout/',views.logoutPage,name="logout")
]