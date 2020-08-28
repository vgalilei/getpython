from django.contrib import admin
from django.urls import path, include
from shortcut.urls import urlpatterns as shortcut_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(shortcut_urls)),
]
