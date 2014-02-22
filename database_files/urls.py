from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<name>.+)$', 'database_files.views.serve', name='database_file'),
)
