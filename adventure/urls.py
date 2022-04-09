
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommender/', include('recommender.urls')),
    path('mapper/', include('mapper.urls')),
    path('', include('authentication.urls')),
]
