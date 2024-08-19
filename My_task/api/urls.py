from django.urls import path
from . import views

urlpatterns = [
    
    path("api_view/",views.app_api.as_view(),name="api_view"),
    path("api_rud/<int:pk>/",views.RUD.as_view(),name="api_rud")

]