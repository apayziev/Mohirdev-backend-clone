import debug_toolbar
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from django.contrib.auth.decorators import login_required
from common.ckeditor_views import browse, upload



API_TITLE = 'Mohirdev API'
API_DESCRIPTION = 'A Web API for creating and editing.'
schema_view = get_swagger_view(title=API_TITLE)

schema_view = get_schema_view(title='Mohirdev API')

urlpatterns = [
    re_path("ckeditor/upload/", login_required(upload), name="ckeditor_upload"),
    re_path(
        "ckeditor/browse/",
        login_required(browse),
        name="ckeditor_browse",
    ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('docs/', include_docs_urls(title=API_TITLE, 
                                    description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view),
]

# MEDIA URLS
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)