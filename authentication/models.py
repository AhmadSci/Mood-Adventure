from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import Point

    
class User(AbstractUser):
    recommendations = models.ManyToManyField('Recommendation', blank=True)
    location = gis_models.PointField(default=Point(0.0, 0.0))
    old_recommendations = models.ManyToManyField('Recommendation', blank=True, related_name='old_recommendations')

class Recommendation(gis_models.Model):
    id = gis_models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=500)
    location = gis_models.PointField()
    link = models.CharField(max_length=5000, blank=True)

