from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
    path('blog/', include('news_blog.urls')),
]
