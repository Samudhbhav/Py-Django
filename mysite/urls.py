from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import *
from mysite.views import current_datetime, hours_ahead

urlpatterns = patterns(' ',
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,3})/$',hours_ahead),
)

# Import the utility functions from the django urls library
from django.conf.urls import patterns, include, url

# Define the url patterns and the corresponding views of this application in
# urlpatterns variable.
urlpatterns = patterns('',
                      # The regex for the root URL / is '^$' which matches nothing
                      # after /.
                      # Map the root URL to be handled by the contact_form view method
                      # in views.py of contact_form app.
                      url(r'^$', 'contact_form.views.contact_form'),
)






