from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'^polls/', include('polls.urls')),
    path(r'^admin/', admin.site.urls),
]