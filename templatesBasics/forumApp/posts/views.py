from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render



# def index(request):
#     return HttpResponse(f"Welcome to the forum app!")

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
    return render(request, 'base.html')
