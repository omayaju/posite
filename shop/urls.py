from django.conf.urls import url, patterns, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^shop/$','shop.views.shop', name = 'shop'),
	url(r'^shop/category/get/(?P<category_id>\d+)/$', 'shop.views.get_category_cont', name = 'get_category_cont'),
	url(r'^shop/product/get/(?P<product_id>\d+)/$', 'shop.views.get_product_cont', name = 'get_product_cont'),
	url(r'^basket/$','shop.views.basket', name = 'basket'),
	url(r'^shop/product/add_to_basket/(?P<product_id>\d+)/$', 'shop.views.add', name = 'add'),
	url(r'^basket/delete/(?P<product_id>\d+)/$', 'shop.views.delete', name = 'delete'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)