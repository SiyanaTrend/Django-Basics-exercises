from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect, reverse

from department.models import Department


def index(request):
    return HttpResponse("<h1>Home page</h1>")

def show_department_by_id(request, pk: int):
    return HttpResponse(f"<h1>Department by ID: {pk}<h1>")


def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f'<h1>Department from slug: {department} </h1>')


def view_with_pk_slug(request, pk, slug):
    # # Option 1 for error 404 => file with name 404.html should be shown,
    # when:
    # DEBUG = False
    # ALLOWED_HOSTS = ['*'] => use it only when testing, never in production. It means everybody can send us requests
    departments = Department.objects.filter(pk=pk, slug=slug)
    if not departments:
        raise Http404
    return HttpResponse(f'<h1>ID: {pk} Department: {departments.first()} </h1>')

    # # Option 2
    # department = get_object_or_404(Department, pk=pk, slug=slug)
    # return HttpResponse(f'<h1>ID: {pk} Department: {department} </h1>')

    # # Option 3
    # return HttpResponseNotFound()


def view_with_regex(request, archive_year: int):
    return HttpResponse(f'The year is: {archive_year}')


def view_with_name(request, variable):
    # return HttpResponse(f'<h1>View with name: {variable} </h1>')
    return render(request, 'departments/name_department.html', {'variable': variable})


def view_with_path(request, variable):
    return HttpResponse(f'<h1>View with path: {variable} </h1>')


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_to_home_page(request):
    # # option 1 - breaks abstractions
    # return redirect('http://localhost:8000', permanent=True)

    # # option 2 breaks single responsibility if view is from another app
    # return redirect(index, permanent=True)

    # option 3 - best option => put a name in urls path: path('', views.index, name='home')
    # when using permanent=True => the data is cashed
    return redirect('home', permanent=True)
