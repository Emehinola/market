from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'professionals/', views.professionals, name='professionals'),
    url(r'hire/', views.hire, name='hire'),
    url(r'resume/', views.resume, name='resume'),
    url(r'', views.accommodation, name='accommodation')
]
