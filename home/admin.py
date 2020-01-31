from django.contrib import admin
from home import models


# Register your models here.
admin.site.register(models.Movie)
admin.site.register(models.MovieReview)
admin.site.register(models.StreamingService)
