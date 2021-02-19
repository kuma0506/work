from django.urls import path
from . import views

app_name = 'startapp_1'
urlpatterns = [
    path('', views.index, name='index'),

]
