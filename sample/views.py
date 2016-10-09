from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader, RequestContext

import json


def response(request):
    return HttpResponse(json.dumps({"status": "success"}), content_type="application/json", status=200)
