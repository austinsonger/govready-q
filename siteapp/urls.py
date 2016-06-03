from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import siteapp.views as views

urlpatterns = [
    url(r"^$", views.homepage),

    # apps
    url(r"^tasks/", include("guidedmodules.urls")),
    url(r"^discussion/", include("discussion.urls")),

    # projects
    url(r'new-project$', views.new_project),
    url(r'projects/(?:(\d+)/(?:[\w\-]+)|system)?$', views.project),

    # invitations
    url(r'invitation/_send$', views.send_invitation, name="send_invitation"),
    url(r'invitation/_cancel$', views.cancel_invitation, name="cancel_invitation"),
    url(r'invitation/(?P<code>.*)$', views.accept_invitation, name="accept_invitation"),

    # auth
	url('^login/$', views.login_view, name='login'),
    url('^', include('django.contrib.auth.urls')),

    # admin site
    url(r'^admin/', include(admin.site.urls)),
]
