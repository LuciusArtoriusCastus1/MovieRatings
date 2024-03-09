def get_celebrity_photos(instance, file):
    return f'celebrities/photos/{instance.celebrity}/{file}'


def get_celebrity_videos(instance, file):
    return f'celebrities/videos/{instance.celebrity}/{file}'


def get_celebrity_image(instance, file):
    return f'celebrities/images/{instance.name}/{file}'
