
from django.urls import path
from . import views
urlpatterns=[
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path("submit_form", views.submit_form, name="submit_form"),
    path("django_form/", views.django_form, name="django_form"),
    path("student_data/", views.student_data_form, name="student_data"),
]