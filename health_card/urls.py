from django.conf.urls import patterns, url
from health_card import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_health_card/$', views.add_health_card, name='add_health_card'),)