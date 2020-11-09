from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.new_list, name='new_list'),
    url('^admin/', admin.site.urls),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.new_body, name='new_body'),
]
