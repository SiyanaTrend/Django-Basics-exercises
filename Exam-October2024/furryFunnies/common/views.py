from django.shortcuts import render

from common.utils import get_profile
from posts.models import Post


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'common/index.html', context)

def dashboard(request):
    profile = get_profile()
    posts = Post.objects.all()

    context = {
        'profile': profile,
        'posts': posts
    }

    return render(request, 'common/dashboard.html', context)
