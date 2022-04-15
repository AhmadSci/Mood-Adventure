import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    lat = request.user.location.y
    long = request.user.location.x
    user_location = request.user.location
    queryset = request.user.old_recommendations.annotate(distance=Distance('location',user_location)).order_by('distance')[0:6]
    return render(request, 'userprofile/index.html' , context={'long': long, 'lat': lat, 'recommendations': queryset})

def update_location(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            long = body['long']
            lat = body['lat']

            point = Point(float(long), float(lat))
            #update users location in database 
            request.user.location = point
            request.user.save()
            return JsonResponse({'status': 'success'})

def delete_recommendation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            pk = body['pk']
            recommendation = request.user.old_recommendations.get(pk=pk)
            recommendation.delete()
            return JsonResponse({'status': 'success'})