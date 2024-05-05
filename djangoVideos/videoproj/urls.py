from django.contrib import admin
from django.urls import path, include
from videoupload.views import videospage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videoupload.urls')),
    
]
