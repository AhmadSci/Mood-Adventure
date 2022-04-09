from django.urls import path
from recommender import views


urlpatterns = [
    path('', views.index, name='index'),
    path('location/', views.update_location, name='location_async'),
    # path('recommendations/', views.get_recommendations, name='recommendations_async'),
]
