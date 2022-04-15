from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Recommendation, User

# Register your models here.

@admin.register(User)
class UserAdmin(OSMGeoAdmin):
    list_display = ('username', 'location')

@admin.register(Recommendation)
class RecommendationAdmin(OSMGeoAdmin):
    list_display = ('description', 'location')