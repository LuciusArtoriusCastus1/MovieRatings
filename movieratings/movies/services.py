def get_movie_photo(instance, file):
    return f'movies/photos/{instance.movie}/{file}'


def get_movie_video(instance, file):
    return f'movies/videos/{instance.movie}/{file}'


def get_movie_trailer(instance, file):
    return f'movies/trailer/{instance.name}/{file}'


def get_movie_poster(instance, file):
    return f'movies/posters/{instance.name}/{file}'
