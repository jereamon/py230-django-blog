from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s" % i for i in kwargs.item()])

    return HttpResponse(body, content_type='text/plain')