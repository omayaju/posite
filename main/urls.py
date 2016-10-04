from django.conf.urls import url, patterns, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$','main.views.index', name = 'index'),
	url(r'^about/$','main.views.about', name = 'about'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)