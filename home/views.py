from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home import models


@login_required
def index(request):
    movie_list = models.Movie.objects.all()
    streaming_list = models.StreamingService.objects.all()
    return render(
        request,
        "home/index.html",
        {"movie_list": movie_list, "streaming_list": streaming_list},
    )
