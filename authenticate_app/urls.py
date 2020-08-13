from django.urls import path
from . import views


urlpatterns =[
    path('login/',views.loginPage,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='welcome'),
    path('logout/',views.logoutPage,name="logout")
]