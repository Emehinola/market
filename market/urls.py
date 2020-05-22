"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from marketplace import views as market_views
from user import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'market/', include('marketplace.urls')),
    url(r'shop/', market_views.shop, name='shop'),
    url(r'personal shops/', market_views.myShop, name='my-shop'),
    url(r'vacancy/', include('vacancy.urls')),
    url(r'services/', include('services.urls')),
    url(r'home/', include('index.urls')),
    url(r'blog/', include('blog.urls')),
    url(r'register/', user_views.register, name='register'),
    url(r'login/', user_views.login_request, name='login'),
    url('', include('index.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)