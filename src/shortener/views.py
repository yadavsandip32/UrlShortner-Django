from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def kirr_redirect_view(request, *args, **kwargs):
    return HttpResponse("Hello")

class KirrRedirectView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")