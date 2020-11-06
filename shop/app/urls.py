from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url('category', views.product_list_view, name='category'),
    url('category/product_id', views.product_detail_view, name='detail')

    # url(r'^$', views.product_list_view.as_view(), name='index'),
    # url(r'^(?P<category>\w*)$', views.product_list_view.as_view(), name='category'),
    # url(r'^(?P<category>\w*)/(?P<product_id>\d*)$', views.product_detail_view.as_view(), name='detail'),

]
