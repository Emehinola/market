from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'computers/', views.computer, name="computers"),
    url(r'phones/', views.phone, name="phones"),
    url(r'electronics/', views.electronics, name="electronics"),
    url(r'fashion/', views.fashion, name="fashion"),
    url(r'accessories/', views.accessories, name="accessories"),
    url(r'add-product/', views.add_product, name="add-product"),
    url(r'product', views.product, name="product"),
    url(r'', views.market, name='market'),
]
