from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/blog/', include('blog.urls')),
]
