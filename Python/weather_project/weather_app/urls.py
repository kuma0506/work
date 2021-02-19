from django.urls import path
from . import views

app_name = 'weather_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    # Ajax処理
    path('every_hours_ajax/', views.every_hours_ajax, name='every_hours_ajax'),
]
