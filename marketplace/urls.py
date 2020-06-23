from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'computers/', views.computer, name="computers"),
    url(r'phones/', views.phone, name="phones"),
    url(r'electronics/', views.electronics, name="electronics"),
    url(r'fashion/', views.fashion, name="fashion"),
    url(r'accessories/', views.accessories, name="accessories"),
    url(r'product/(?P<id>\d+)$', views.product, name="single product"),
    url(r'add-product/', views.add_product, name="add-product"),
    url(r'checkout/(?P<id>\d+)$', views.checkout, name="checkout"),
    url(r'', views.market, name='market'),
]
