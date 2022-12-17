from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('audios/', AudiosApiView.as_view(), name='audios'),
    path('topics/', TopicsApiView.as_view(), name='topics'),
    path('topic/<int:pk>/audios/', TopicAudiosApiView.as_view(), name='topic-audios'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


