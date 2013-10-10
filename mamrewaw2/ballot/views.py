from django.shortcuts import render_to_response

def landing(request, uuid):
    return render_to_response('ballot/landing.html', {'uuid': uuid})
