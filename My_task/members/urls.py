from django.urls import path
from. import views
urlpatterns = [
# Create your views here.
    path("",views.login_reg,name="login_reg")
]