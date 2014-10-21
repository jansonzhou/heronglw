from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from heronglw import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('product.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
