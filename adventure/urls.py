
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommender/', include('recommender.urls')),
    path('mapper/', include('mapper.urls')),
    path('', include('authentication.urls')),
    path('profile/', include('userprofile.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
