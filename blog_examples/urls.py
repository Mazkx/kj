from django.conf.urls import  include, url


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^image_uploader/', include('image_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

#if settings.DEBUG:
#    urlpatterns += ['',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.MEDIA_ROOT,
#        }),
#        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.STATIC_ROOT,
#        })
#   ]
#
#if  settings.DEBUG:
# urlpatterns += ['',  url(r'^media/(?P<path>.*)$', include('django.views.static.serve')),      url(r'^static/(?P<path>.*)$', include('django.views.static.serve'))   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#

 
