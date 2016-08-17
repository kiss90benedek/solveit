from django.conf.urls import url

from . import api, views

urlpatterns = [
    url(r'^create', views.create),
    url(r'^api/create', api.create_new_category),
]
