from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('choose_campus', views.choose_campus, name='choose_campus'),
    path('choose_location', views.choose_location, name='choose_location'),
    path('dc_floor_plan', views.dc_floor_plan, name='dc_floor_plan'),
    path('choose_queens', views.choose_queens, name='choose_queens'),
    path('choose_western', views.choose_western, name='choose_western'),
    path('dp_floor_plan', views.dp_floor_plan, name='dp_floor_plan'),
]
