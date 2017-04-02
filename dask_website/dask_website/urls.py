from django.conf.urls.defaults import *
import registration

urlpatterns = patterns('',
    # Example:
    # (r'^dj_project/', include('dj_project.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^dj_survey/', include('dj_project.dj_survey.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^yui/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': '../../svn_views/yui/build','show_indexes': True
    }),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': './media','show_indexes': True
    }),
)
