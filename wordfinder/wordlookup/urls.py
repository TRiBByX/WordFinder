from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^', views.WordFinder.as_view(), name='wfinder'),
]
