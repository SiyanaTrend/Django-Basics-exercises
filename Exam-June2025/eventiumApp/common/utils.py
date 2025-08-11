from organizer.models import Organizer


def get_profile():
    return Organizer.objects.first()
