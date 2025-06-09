from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 1.90,
        },
        "IDs": ["1223", "exe1234", "si5684"],
        "some_text": "everything works well!",
        "no_text": "",
        "users": ["pesho", "ivan", "stamat", "maria", "magdalena"]
    }
    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create Django project",
                "author": "Maria Kirilova",
                "content": "",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create HTML file ",
                "author": "Ivan Abadjiev",
                "content": "It is the **most easiest** <i>thing</i> to do",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create CSS file",
                "author": "",
                "content": "### You should follow my steps",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'dashboard.html', context)
