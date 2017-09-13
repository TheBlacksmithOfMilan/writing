from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {"template_name": "account/login.html", "redirect_authenticated_user": True}, name='login'),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name='logout'),
]
