import json
import requests
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from authentication.models import Recommendation

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    long = request.user.location.x
    lat = request.user.location.y
    return render(request, 'recommender/index.html',context= {'long': long, 'lat': lat})

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


# api_key = 'API_KEY'
# def get_recommendations(request):
#     url = "https://maps.googleapis.com/maps/api/place/details/json?"
#     if request.method == 'POST':
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         query = body['query']
#         placeid = recommend(query,request.user.location.x,request.user.location.y)

#     # r = requests.get(url + 'place_id=' + placeid + '&key=' + api_key)

#     # x = r.json()
    
#     # y = x.result.geometry.location
#     # Recommendation.objects.create(id=placeid, description=query, location=Point(y.lng,y.lat))
#     # rec = Recommendation.objects.filter(id=placeid)
#     # request.user.recommendations.add(rec)
#     # request.user.save()
#     return (placeid)

# def recommend(query,x,y):
#     url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
#     location = str(y)+'%2C'+str(x)
    
#     # get method of requests module
#     # return response object
#     r = requests.get(url + 'location=' + location + '&query=' + query + '&key=' + api_key)
    
#     # json method of response object convert
#     #  json format data into python format data
#     res = r.json()
#     print (res)

    
#     # now x contains list of nested dictionaries
#     # we know dictionary contain key value pair
#     # store the value of result key in variable y
#     ress = res['results']
    
#     # keep looping upto length of y
#     return ress
