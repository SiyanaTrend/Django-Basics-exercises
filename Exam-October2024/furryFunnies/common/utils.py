from authors.models import Author


def get_profile():
    return Author.objects.first()
