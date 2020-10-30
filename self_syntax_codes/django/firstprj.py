#urls.py

from django.contrib import admin
#from django.urls import path				#doesn't allow regex
from django.conf.urls import url			#allows regex in url
from mysite.views import current_datetime
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time/$', current_datetime),
    url(r'^hundred/plus/(\d{1,2})/$', add_hundred),
]


######################################################################################################################################################

#views.py

from django.http import HttpResponse
import datetime

def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

def add_hundred(request,value):
        try:
                value = int(value)
        except ValueError:
                raise Http404()
        new_value=100+value
        html = "<html><body>Adding 100 to %s will give %s.</body></html>" % (value, new_value)
        return HttpResponse(html)
