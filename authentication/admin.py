from django.contrib import admin

from .models import Recommendation, User

# Register your models here.

admin.site.register(Recommendation)
admin.site.register(User)
