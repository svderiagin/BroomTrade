from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^$', include('main.urls')),
    url(r'^guestbook/', include('guestbook.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^imagepool/', include('imagepool.urls')),
    url(r'^categories/', include('categories.urls')),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
