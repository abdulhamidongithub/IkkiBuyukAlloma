from django.contrib import admin
from django.urls import path
from asosiy.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Ikki buyuk alloma API",
      default_version='v1',
      description="Ikki buyuk alloma ilovasi uchun yozilgan API",
      contact=openapi.Contact(email="1997abdulhamid@gmail.com"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('audios/', AudiosApiView.as_view(), name='audios'),
    path('topics/', TopicsApiView.as_view(), name='topics'),
    path('topic/<int:pk>/audios/', TopicAudiosApiView.as_view(), name='topic-audios'),
    path('sayyidsafo_docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


