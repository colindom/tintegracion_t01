from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('walt/', include('walt.urls')),
    path('admin/', admin.site.urls),
]