from django.urls import path
from. import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.index,name="index"),
    path("interface/",views.interface,name="interface"),
    path("details/<task_id>",views.details,name="details"),
    path("task/",views.counter,name="task"),
    path("logout",views.user_logout,name="logout"),
    
]
