from players.models import Player


def get_profile():
    return Player.objects.first()
