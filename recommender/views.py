import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.gis.geos import Point

from authentication.models import Recommendation

from selenium import webdriver
from parsel import Selector
import random



def index(request):
    # check if user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')
    # getting user's location 
    long = request.user.location.x
    lat = request.user.location.y
    return render(request, 'recommender/index.html',context= {'long': long, 'lat': lat})


# making a query from the user's inputs
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
                recommendation += " close by"

            return JsonResponse({'status': recommendation})

link = ""
name = ""
lat = ""
long = ""
def chormiuimsearch(url):
    # setting the variables
    global link
    global name
    global lat
    global long
    link = ""
    name = ""
    chromedrive_path = './chromedriver.exe'

    #setting up the chrome driver
    options = webdriver.ChromeOptions()

    options.add_argument('headless')
    browser = webdriver.Chrome(chromedrive_path,options=options)
    browser.get(url)

    # getting the html of the page
    page_content = browser.page_source
    response = Selector(page_content)

    # generating a random number to choose a random place to visit
    num = random.randrange(3, 20, 2)
    
    # getting the link and the name of the place
    for el in response.xpath(f'//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[{num}]/div/a'):
        link += el.xpath('./@href').extract_first('')+"&hl=en"
        name += el.xpath('./@aria-label').extract_first('')
    
    # trying to get the lat and long of the place
    try:
        long = link[link.index("!3d")+len("123"):link.index("!4d")]
        lat = link[link.index("!4d")+len("123"):link.index("?auth")]
    except ValueError:
    # if the place is not found, then try again
        chormiuimsearch(url)

    browser.quit()

def get_recommendations(request):
    x = request.user.location.x
    y = request.user.location.y
    if request.method == 'POST':
        # getting the request and processing it
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        query = body['query']
        url = f"https://www.google.com/maps/search/{query}/@{y},{x}"

        # getting the recommendations from google maps using selenium
        chormiuimsearch(url)

        # make a point with long ad lat and add to to user's recommendation list 
        point = Point(float(lat), float(long))

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
