from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home/', include('webapp.urls')),
    path('nest/', include('webapp.urls')),
    path('admin/', admin.site.urls),
]