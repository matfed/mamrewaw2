from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import datetime, date
from events.models import Event, Location
from django.shortcuts import get_object_or_404

def index(request):
    event_list = Event.objects.filter(start_date__gte=datetime.now().date()).order_by('start_date')
    grouped_events = groupEvents(event_list)
    location_list = Location.objects.all()
    return render_to_response('events/index.html', 
                              {'event_list': event_list, 'grouped_events': grouped_events, 'location_list': location_list}, 
                              context_instance=RequestContext(request))

def groupEvents(event_list):
    last_group = None
    grouped_events = []
    for event in event_list:
        group = (event.start_date.year, event.start_date.month)
        if group != last_group:
            grouped_events.append((date(group[0], group[1], 1), []))
            last_group = group
        grouped_events[-1][1].append(event)
    return grouped_events

def archive(request):
    event_list = Event.objects.all().order_by('start_date')
    return render_to_response('events/archive.html', {'event_list': event_list}, context_instance=RequestContext(request))

def detail(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render_to_response('events/detail.html', {'event': e}, context_instance=RequestContext(request))

def locations(request):
    location_list = Location.objects.all()
    return render_to_response('events/locations.html', {'location_list': location_list}, context_instance=RequestContext(request))