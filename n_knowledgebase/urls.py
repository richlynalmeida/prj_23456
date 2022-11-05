from django.urls import path, include
from . import views


app_name = "n_knowledgebase"


urlpatterns = [
    path('n_knowledgebase/', views.home, name='n_knowledgebase'),

]
