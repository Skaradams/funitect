import os

from django.conf.urls.defaults import *
from django.contrib import admin

from tastypie.api import Api

from funitect.service import views
from funitect import settings

admin.autodiscover()
api = Api(api_name='v1')


for resource_name in views.__all__:
    api.register(getattr(views, resource_name)())

urlpatterns = patterns('',
    url(r'^upload-sketch/$', 'funitect.service.views.upload_sketch'),
    (r'^api/', include(api.urls)),
    (r'^admin/', include(admin.site.urls)),
    url(r'^sketches/(.*)$', 'django.views.static.serve', {
        'document_root': settings.SKETCHES_DIR,
        'show_indexes': False
    }),
    url(r'^(.*)$', 'django.views.static.serve', {
        'document_root': os.path.join(os.path.dirname(__file__), 'front'),
        'show_indexes': True
    }),
)
