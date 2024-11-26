from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns  = [
    path('', views.home, name="home"),
    #path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('members/<int:pk>', views.member_records, name="members"),
    path('delete_members/<int:pk>', views.delete_members, name="del_members"),
    path('add_members/', views.add_members, name="add_members"),
    path('update_members/<int:pk>', views.update_members, name="update_members"),
    
]