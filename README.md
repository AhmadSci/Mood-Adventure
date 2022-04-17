
# Mood-Adventure

A Django Web application that recommends a mini adventure based on your current mood using GeoDjango.

# Features

- [x] User can login and logout
- [x] User can create a new account
- [x] User can set their location in their `profile` page
- [x] User can get an adventure recommendation based on their mood and mode of transportation
- [x] User can view all the recommendations they got in the `Previous Recommendations` Page
- [x] User can delete any recommendation they didnt like from their `profile` page
- [x] A clean minimalistic user interface using Bootstrap

# Installation

1- Download these programs 
- [osgeo4w](https://trac.osgeo.org/osgeo4w/) *to install all geodjango's needed packages*
- [docker](https://www.docker.com/products/docker-desktop/) *to install docker*
- [wsl_update_x64](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) *to install the wsl linux update that is needed by docker*

2- Create the database
```bash
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```

3- Create a virtual environment and activate it 
```bash
python -m venv env
env\Scripts\activate
```

4- Install the requirements

```bash
pip install -r requirements.txt
```

5- Run these commands
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6- Finally run the server
```bash
python manage.py runserver
```

# Preview

## Home Page
![Home Page](/media/HomePage.png)

## Recommendation Page
![Recommendatin Page](/media/Recommendation_view.png)

## Previous Recommendations Page
![Recommendatin Page](/media/Previous_Recommendations.png)

## Profile Page
![Recommendatin Page](/media/Profile_Page.png)

# Credits

[Making a location based app with Django and GeoDjango](https://realpython.com/location-based-app-with-geodjango-tutorial/)