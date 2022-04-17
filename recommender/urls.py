from django.urls import path
from recommender import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process_recommendation, name='process_recommend_async'),
    path('recommendations/', views.get_recommendations, name='recommendations_async'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)