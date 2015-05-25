from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lkd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'lkd.views.index'),
    url(r'^new$', 'lkd.views.new', name='new'),
    url(r'^user/(?P<id>[^\.]+)', 'userprofile.views.view_user', name='view_user'),
    url(r'^view/(?P<id>[^\.]+)', 'link.views.view_link', name='view_link'),
    url(r'^click/(?P<id>[^\.]+)', 'link.views.redirect_link', name='redirect_link'),
    url(r'^category/(?P<slug>[^\.]+)', 'link.views.view_link_category', name='view_link_category'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'', include('social_auth.urls')),
)