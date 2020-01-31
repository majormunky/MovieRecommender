from django.db import models
from django.conf import settings


class StreamingService(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    service = models.ForeignKey(
        StreamingService, on_delete=models.PROTECT, blank=True, null=True
    )
    reviewed_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="MovieReview"
    )


class MovieReview(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
