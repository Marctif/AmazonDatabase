from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('Amazon_Core.urls')),
url(r'^accounts/', include('allauth.urls')),
]
