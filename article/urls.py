from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^list$', views.article_list, name='article_list'),
    url(r'^my/list$', views.my_article_list, name='my_article_list'),
    url(r'^(?P<id>\d+)/post/list$', views.article_post_list, name='article_post_list'),
    url(r'^create$', views.article_create, name='article_create'),
    url(r'^(?P<id>\d+)/comment$', views.article_comment, name='article_comment'),
    url(r'^(?P<id>\d+)/v/(?P<vid>\d+)/comment$', views.article_post_comment, name='article_post_comment'),
    url(r'^(?P<id>\d+)/v/(?P<vid>\d+)/edit$', views.article_edit, name='article_edit'),
    url(r'^(?P<id>\d+)/v/(?P<vid>\d+)/reedit$', views.article_reedit, name='article_reedit'),
    url(r'^(?P<id>\d+)/body$', views.article_post_body, name='article_post_body'),
    url(r'^(?P<id>\d+)/v/(?P<vid>\d+)/comment/list$', views.article_comment_list, name='article_comment_list'),

]
