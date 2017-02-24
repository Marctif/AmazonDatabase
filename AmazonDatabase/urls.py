from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# ... your normal urlpatterns here

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('Amazon_Core.urls')),
    url(r'^accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


