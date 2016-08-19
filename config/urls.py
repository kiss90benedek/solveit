from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog

i18n_urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/categories$',
        JavaScriptCatalog.as_view(packages=['categories']),
        name='javascript-catalog'),
]

urlpatterns = [
    url(r'^', include('solveit.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^', include(i18n_urlpatterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
