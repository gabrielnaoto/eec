from django.conf.urls import url

from core.views import index

urlpatterns = [
    url('^index/$', index, name='index')
]
