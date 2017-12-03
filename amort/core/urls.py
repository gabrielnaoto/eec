from django.conf.urls import url

from amort.core.views import index

urlpatterns = [
    url('^index/$', index, name='index')
]
