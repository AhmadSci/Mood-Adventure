from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('location/', views.update_location, name='location_async'),
    path('delete/', views.delete_recommendation, name='delete_recommendation'),
]
