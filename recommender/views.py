import json
from operator import contains
import requests
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from authentication.models import Recommendation

from selenium import webdriver
from parsel import Selector
import random

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    long = request.user.location.x
    lat = request.user.location.y
    return render(request, 'recommender/index.html',context= {'long': long, 'lat': lat})

def process_recommendation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            recommendation = "places to visit while being "
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            mood = body['mood']

            if "happy" in mood.lower():
                recommendation += "happy"
            if "sad" in mood.lower():
                recommendation += "sad"
            if "curious" in mood.lower():
                recommendation += "curious"
            if "bored" in mood.lower():
                recommendation += "bored"
            if "mad" in mood.lower():
                recommendation += "mad"

            if "walking" in mood.lower():
                recommendation += " near me"
            if "car" in mood.lower():
                recommendation += " in my city"

            return JsonResponse({'status': recommendation})

            


def get_recommendations(request):
    x = request.user.location.x
    y = request.user.location.y
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        query = body['query']
        url = f"https://www.google.com/maps/search/{query}/@{y},{x}"
        chromedrive_path = './chromedriver.exe'
        options = webdriver.ChromeOptions()

        options.add_argument('headless')
        browser = webdriver.Chrome(chromedrive_path,options=options)
        browser.get(url)

        page_content = browser.page_source
        response = Selector(page_content)

        num = random.randrange(3, 10, 2)
        print(num)
        link = ""
        name = ""

        for el in response.xpath(f'//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[{num}]/div/a'):
            link += el.xpath('./@href').extract_first('')+"&hl=en"
            name += el.xpath('./@aria-label').extract_first('')
        print(request.user.location.x)
        print(request.user.location.y)
        print(url)
        print(link)
        long = link[link.index("!3d")+len("123"):link.index("!4d")]
        lat = link[link.index("!4d")+len("123"):link.index("?auth")]
        print(float(long))
        print(float(lat))
        browser.quit()

        # make a point with long ad lat and add to to user's recommendation list 
        point = Point(float(lat), float(long))
        print(point)
        recommendation = Recommendation(location=point, description=name, link=link)
        recommendation.save()
        # add recommendation to user's list of previous recommendations
        request.user.old_recommendations.add(recommendation)
        # remove all recommendations from user's list
        request.user.recommendations.clear()
        # add new recommendation to user's list
        request.user.recommendations.add(recommendation)
        request.user.save()

    return JsonResponse({'url': url, "name": name})
