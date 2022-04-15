from django.shortcuts import redirect, render
from django.contrib.gis.db.models.functions import Distance
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_location = request.user.location
    queryset = request.user.recommendations.annotate(distance=Distance('location',user_location)).order_by('distance')[0:6]
    long = user_location.x
    lat = user_location.y
    return render(request, 'mapper/index.html', context= {'recommendations': queryset, 'long': long, 'lat': lat})

def previous(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_location = request.user.location
    queryset = request.user.old_recommendations.annotate(distance=Distance('location',user_location)).order_by('distance')[0:6]
    long = user_location.x
    lat = user_location.y
    return render(request, 'mapper/previous.html', context= {'recommendations': queryset, 'long': long, 'lat': lat})
