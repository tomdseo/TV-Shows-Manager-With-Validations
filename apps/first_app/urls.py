from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.redirect_url), # redirect localhost/8000 to localhost/8000/shows
    url(r'^show$', views.redirect_url), # redirect localhost/8000/show to localhost/8000/shows
    url(r'^shows$', views.read_all_show), # read all page
    url(r'^shows/new$', views.create_show), # create page
    url(r'shows/(?P<id>\d+)$', views.read_one_show), # read one page
    url(r'^shows/add$', views.add_show), # add button
    url(r'^shows/(?P<id>\d+)/update', views.update_show), # update button
    url(r'shows/(?P<id>\d+)/edit', views.edit_show), # update page
    url(r'shows/(?P<id>\d+)/delete', views.delete_show), # delete show
]
