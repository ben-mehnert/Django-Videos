from django.urls import path, include
from videoupload.views import videospage, upload_video
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', videospage, name='all_videos'),
    path('videos/<str:tag_name>/', videospage, name='videos_with_tag'),
    path('upload/', upload_video, name='upload_video'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
