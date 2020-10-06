from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Movie)
admin.site.register(models.Ratings)