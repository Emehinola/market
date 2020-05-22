from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'jobs/', views.jobs, name='jobs'),
    url(r'job/', views.job, name='job'),
    url(r'job-post/', views.job_post, name='job-post'),
    url(r'', views.vacancy, name='vacancy')
]