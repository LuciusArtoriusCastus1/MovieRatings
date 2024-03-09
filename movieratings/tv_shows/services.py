def get_tv_show_photo(instance, file):
    return f'tvshow/photos/{instance.tv_show}/{file}'


def get_tv_show_video(instance, file):
    return f'tvshow/videos/{instance.tv_show}/{file}'


def get_tv_show_trailer(instance, file):
    return f'tvshow/trailer/{instance.name}/{file}'


def get_tv_show_poster(instance, file):
    return f'tvshow/posters/{instance.name}/{file}'


def get_tv_episode_photo(instance, file):
    return f'tvshow/episodes/photos/{instance.tv_episode}/{file}'


def get_tv_episode_video(instance, file):
    return f'tvshow/episodes/videos/{instance.tv_eisode}/{file}'


def get_tv_episode_trailer(instance, file):
    return f'tvshow/episodes/trailer/{instance.name}/{file}'


def get_tv_episode_poster(instance, file):
    return f'tvshow/episodes/posters/{instance.name}/{file}'
