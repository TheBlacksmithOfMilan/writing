from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def home(request):
    return HttpResponseRedirect(reverse('article:article_list'))



# Create your views here.
