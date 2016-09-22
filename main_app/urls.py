from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    # Not checking for any path -- would match 'localhost':
    url(r'^$', views.index, name = 'index'),
    # This URL REGEX looks for a number and captures that value to send to the detail view -- would match e.g., 'localhost/15'
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    # Form submission (localhost/post_url):
    url(r'^post_url/$', views.post_treasure, name = 'post_treasure'),
    # User profile page at localhost/user/user_name:
    # Regex (\w+) will capture a word of any length.
    url(r'^user/(\w+)/$', views.profile, name = 'profile'),
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^like_treasure/$', views.like_treasure, name = 'like_treasure'),
]

# The URL pattern below allows us to serve files (other than static files) in development (indicated by .DEBUG).
# Importing the serve view allows us to use it to send any URL that matches media/ to a built-in Django view called static.serve()
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    ]
    # urlpatterns += patterns('',
    #     url(r'^media/(?P<path>,*)$', serve, { 'document_root': settings.MEDIA_ROOT,
    #     }),
    #     url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,
    #     }),
    # )
