from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('video/', include('video.urls')),
    path('', include('login.urls')),

    path('admin/', admin.site.urls)
]

# Обработчик ошибки 404
handler404 = 'main.views.custom_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)