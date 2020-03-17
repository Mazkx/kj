from django.conf.urls import  url
from .views import UploadURLView, UploadDetailView

urlpatterns = [
    url(r'^$', UploadURLView.as_view(), name="upload-url"),
    url(r'^show/(?P<pk>\d+)/$', UploadDetailView.as_view(), name="upload-detail"),
]
