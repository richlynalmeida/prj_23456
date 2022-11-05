from django.urls import path, include
from . import views


app_name = "csl"


urlpatterns = [
    path('', views.home, name='home'),

]
