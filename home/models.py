from django.db import models
from django.conf import settings


class StreamingService(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class TelevisionShow(models.Model):
    title = models.CharField(max_length=64, unique=True)
    service = models.ForeignKey(
        StreamingService, on_delete=models.PROTECT, blank=True, null=True
    )
    reviewed_by = models.ManyToManyField(settings.AUTH_USER_MODEL, through="ShowReview")

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    service = models.ForeignKey(
        StreamingService, on_delete=models.PROTECT, blank=True, null=True
    )
    reviewed_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="MovieReview"
    )

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class ShowReview(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    show = models.ForeignKey(TelevisionShow, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
