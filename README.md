
# Mood-Adventure

A Django Web application that recommends a mini adventure based on your current mood.


# Installation

1- Download these programs 
- [docker](https://www.docker.com/products/docker-desktop/)
- [osgeo4w](https://trac.osgeo.org/osgeo4w/)
- [wsl_update_x64](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

2- Create the database
```bash
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```

3- Activate the virtual environment 
```bash
source env\Scripts\activate
```
OR
Create a virtual environment
```bash
python -m venv env
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