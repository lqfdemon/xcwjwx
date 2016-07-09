from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xcwj_wechat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^health_card/', include('health_card.urls')),  # ADD THIS NEW TUPLE!
    url(r'^news/', include('news.urls')),
)
