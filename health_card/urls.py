from django.conf.urls import patterns, url
from health_card import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_health_card/$', views.add_health_card, name='add_health_card'),
        url(r'^test_wechat/$', views.test_wechat, name='test_wechat'),
        url(r'^test_m_url/(\d{1,2})/(\d[1,3])/$',views.test_m_url,name='test_m_url'),
        )