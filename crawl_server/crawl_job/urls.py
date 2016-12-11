from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.crawl_point, name='crawl_point')
]
