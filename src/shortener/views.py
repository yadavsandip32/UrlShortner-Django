from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import KirrURL

def kirr_redirect_view(request,shorturl=None, *args, **kwargs):
    print(shorturl)
    # obj = get_object_or_404(KirrURL, shorturl=shorturl)
    obj = KirrURL.objects.get(shorturl=shorturl)
    return HttpResponseRedirect(obj.url)
