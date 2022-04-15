from django.urls import path
from recommender import views


urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process_recommendation, name='process_recommend_async'),
    path('recommendations/', views.get_recommendations, name='recommendations_async'),
]
