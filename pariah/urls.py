from django.conf.urls.defaults import patterns, url

from pariah import views


urlpatterns = patterns('',
    url(r'^$', views.ComicsView.as_view(), name='comic-list'),
    url(r'^(?P<year>\d{4})/(?P<month>[0-9]{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w ]+)/',
        views.ComicView.as_view(), name='comic-detail'),
)
