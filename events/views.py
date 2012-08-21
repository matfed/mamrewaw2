from datetime import datetime
from events.models import Event, Location
from django.shortcuts import get_object_or_404
from utils import enrich_and_render_to_response

def index(request):
    event_list = Event.objects.filter(start_date__gte=datetime.now().date()).order_by('start_date')
    return enrich_and_render_to_response(request, 'events/index.html', {'event_list': event_list})

def archive(request):
    event_list = Event.objects.all().order_by('start_date')
    return enrich_and_render_to_response(request, 'events/archive.html', {'event_list': event_list})

def detail(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return enrich_and_render_to_response(request, 'events/detail.html', {'event': e})

def locations(request):
    location_list = Location.objects.all()
    return enrich_and_render_to_response(request, 'events/locations.html', {'location_list': location_list})