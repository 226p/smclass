from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('foodBoard/', include('foodBoard.urls')),
    path('map/', include('map.urls')),
    path('board/', include('board.urls')),
    path('member/', include('member.urls')),
    path('comment/', include('comment.urls')),
]


# media 연결
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)