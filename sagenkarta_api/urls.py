from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^documents/', views.getDocuments, name='getDocuments'),
    url(r'^document/(?P<documentId>[^/]+)/$', views.getDocument, name='getDocument'),
]