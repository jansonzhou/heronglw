from django.conf.urls import patterns, include, url
urlpatterns = patterns('product.views',
   url(r'^$', 'index', name='index'),    
)
