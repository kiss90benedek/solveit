from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('solveit.urls')),
    url(r'^categories/', include('categories.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
