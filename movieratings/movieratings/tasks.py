from django.core.mail import send_mail

from custom_user.models import User
from movieratings.celery import app
from movies.models import Movies
from tv_shows.models import TVShow


@app.task
def send_movie_recommendations():
    user_emails = [user.email for user in User.objects.all()]
    trending_movies = [movie.name for movie in Movies.objects.all().order_by('-release_date').order_by('rating')[:3]]
    for email in user_emails:
        send_mail(
            'Trending Movie',
            f'Trending Movie you would like to watch: {", ".join(trending_movies)}!!!',
            'gameaddicted2356@gmail.com',
            recipient_list=[email],
            fail_silently=True
        )


@app.task
def send_tvshow_recommendations():
    user_emails = [user.email for user in User.objects.all()]
    trending_movies = [tvshow.name for tvshow in TVShow.objects.all().order_by('-release_date').order_by('rating')[:3]]
    for email in user_emails:
        send_mail(
            'Trending TVShows',
            f'Trending TVShows you would like to watch: {", ".join(trending_movies)}!!!',
            'gameaddicted2356@gmail.com',
            recipient_list=[email],
            fail_silently=True
        )


