from datetime import datetime

from django.shortcuts import render
from posts.forms import PostBaseForm


def index(request):
    return render(request, 'index.html')

# use with PostForm from the forms.py:
# def index(request):
#     form = PostForm(request.POST or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'index.html', context)


# use with examples from the forms.py:
# def index(request):
#     form = MyFrom(request.POST or None)
#
#     # # equals:
#     # if request.method == 'GET':
#     #     form = MyFrom()
#     # else:
#     #     form = MyFrom(request.POST)
#
#     if form.is_valid():
#         print('The data is', request.POST.get('my_text'))
#         print('The data is', form.cleaned_data.get('my_text'))
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'index.html', context)


def home_page(request):
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
