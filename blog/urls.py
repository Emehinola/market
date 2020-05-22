from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'single/(?P<id>\d+)$', views.single, name="single"),
    url(r'', views.blog, name='blog')
]
