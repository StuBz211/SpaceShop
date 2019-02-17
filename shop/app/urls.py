from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='index'),
    url(r'^(?P<category>\w*)$', views.ProductListView.as_view(), name='category'),
    url(r'^(?P<category>\w*)/(?P<product_id>\d*)$', views.ProductDetailView.as_view(), name='detail'),
]