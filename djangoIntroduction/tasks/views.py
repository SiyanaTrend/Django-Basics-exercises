from django.http import HttpResponse

from django.shortcuts import render

from tasks.models import Task


def index(request):
    search_title = request.GET.get('filter_title', '')

    tasks = Task.objects.filter(name__icontains=search_title)

    context = {
        'search_title': search_title,
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


"""first example:"""
# def index(request):
#     tasks = Task.objects.all()
#     output = '\n'.join([
#         '<h1>TASKS</h1>',
#         '<ul>',
#         *[f"<li>{t.name}: {t.description}" for t in tasks],
#         '</ul>'
#     ])
#     if not output:
#         output = 'There are no created tasks!'
#
#     return HttpResponse(output)
