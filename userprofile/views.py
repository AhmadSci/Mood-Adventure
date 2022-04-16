import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

# getting user's location and recommendations
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    lat = request.user.location.y
    long = request.user.location.x
    user_location = request.user.location
    queryset = request.user.old_recommendations.annotate(distance=Distance('location',user_location)).order_by('distance')[0:6]
    return render(request, 'userprofile/index.html' , context={'long': long, 'lat': lat, 'recommendations': queryset})

# update user's location
def update_location(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        # check if user is posting data
        if request.method == 'POST':
            # get the data from the request and decoding it
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            long = body['long']
            lat = body['lat']

            # make a new point with the user's new location
            point = Point(float(long), float(lat))

            #update users location in database 
            request.user.location = point
            request.user.save()
            return JsonResponse({'status': 'success'})

# delete unwanted recommendations
def delete_recommendation(request):
    # check if user is authenticated
    if request.user.is_authenticated:
        # check if user is posting data
        if request.method == 'POST':
            # get the data from the request and decoding it to get the id of the unwanted recommendation
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            pk = body['pk']

            # delete the unwanted recommendation from the database
            recommendation = request.user.old_recommendations.get(pk=pk)
            recommendation.delete()
            return JsonResponse({'status': 'success'})