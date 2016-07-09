from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
        url(r'^(\d{1,2})/$',views.news_list,name='news_list'),
        )