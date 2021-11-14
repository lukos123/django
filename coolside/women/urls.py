from django.conf.urls.static import static
from django.urls import path

from coolside import settings
from women.views import *

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:num>', public, name='post'),
    path('post/', index),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)