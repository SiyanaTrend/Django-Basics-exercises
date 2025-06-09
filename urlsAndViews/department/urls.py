from django.urls import path, re_path

from department import views

urlpatterns =[
    path('', views.index, name='home'), #http://localhost:8000/departments/
    path('redirect-to-home-page/', views.redirect_to_home_page, name='redirect-view'),
    path('softuni/', views.redirect_to_softuni),
    path('<int:pk>/<slug:slug>/', views.view_with_pk_slug),
    path('<int:pk>/', views.show_department_by_id), #http://localhost:8000/departments/4/
    path('<slug:slug>/', views.view_with_slug), #http://localhost:8000/departments/marketing-department/
    re_path(r'^archive/(?P<archive_year>202[0-4])/$', views.view_with_regex), #http://localhost:8000/departments/archive/2022/ => The year is: 2022
    path('<variable>/', views.view_with_name),  # matches until / => dadadf
    path('<path:variable>/', views.view_with_path),  # matches after the / as well => fsfsdf/fsdfsdfsd/fsfs
]
