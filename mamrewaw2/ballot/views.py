from django.template import RequestContext
from django.shortcuts import render_to_response
from ballot.models import Voter, Candidate, Ballot, Vote
from django.http import HttpResponse, HttpResponseBadRequest

def landing(request, token):
    return render_to_response('ballot/landing.html', {'token': token}, 
                              context_instance=RequestContext(request))

def check(request):
    if request.method != 'POST': 
        return HttpResponseBadRequest()
    errors = []
    token = request.POST.get('token', '')
    if not token:
        return HttpResponseBadRequest()
    pin = request.POST.get('pin', '')
    if not pin:
        errors.append('Podaj PIN.')
    if not errors:
        try:
            voter = Voter.objects.get(token=token, pin=pin)
            if voter.used:
                return render_to_response('ballot/used.html', {'voter': voter}, 
                                          context_instance=RequestContext(request))
            candidates = Candidate.objects.all()
            return render_to_response('ballot/form.html', {'voter': voter, 'candidates': candidates}, 
                                        context_instance=RequestContext(request))
        except Voter.DoesNotExist:
            errors.append('Bledny PIN.')
    return render_to_response('ballot/landing.html', {'token': token, 'errors': errors}, 
                                context_instance=RequestContext(request))
        

def confirm(request):
    if request.method != 'POST': 
        return HttpResponseBadRequest()
    errors = []
    token = request.POST.get('token', '')
    if not token:
        return HttpResponseBadRequest()
    pin = request.POST.get('pin', '')
    if not pin:
        return HttpResponseBadRequest()
    selectedIds = request.POST.getlist('candidate',[])
    if len(selectedIds) > 3:
        errors.append('Mozesz wybrac co najwyzej 3 kandydatow')
    voter = Voter.objects.get(token=token, pin=pin)
    if not errors:
        selected = Candidate.objects.all().filter(id__in=selectedIds)
        return render_to_response('ballot/confirm.html', {'voter': voter, 'selected':selected},
                                  context_instance=RequestContext(request))
    candidates = Candidate.objects.all()
    return render_to_response('ballot/form.html', {'voter': voter, 'candidates': candidates, 'errors': errors}, 
                              context_instance=RequestContext(request))

def finish(request):
    if request.method != 'POST': 
        return HttpResponseBadRequest()
    errors = []
    token = request.POST.get('token', '')
    if not token:
        return HttpResponseBadRequest()
    pin = request.POST.get('pin', '')
    if not pin:
        return HttpResponseBadRequest()
    voter = Voter.objects.get(token=token, pin=pin, used=False)

    selectedIds = request.POST.getlist('candidate',[])
    if len(selectedIds) > 3:
        return HttpResponseBadRequest()
    
    selected = Candidate.objects.all().filter(id__in=selectedIds)
    voter.used = True
    voter.save()
    b = Ballot()
    b.save()
    for candidate in selected:
        v = Vote(ballot=b, candidate=candidate)
        v.save()

    return render_to_response('ballot/thanks.html', {'voter': voter}, context_instance=RequestContext(request))