from django.urls import path
from mapper import views

app_name = 'mapper'

urlpatterns = [
    path('', views.index, name='index'),
    path('previous', views.previous, name='previous'),
]
