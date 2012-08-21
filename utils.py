from datetime import datetime
from events.models import Event
from django.shortcuts import render_to_response

def enrich_and_render_to_response(template, context = {}):
    latest_events_list = Event.objects.filter(start_date__gte=datetime.now().date()).order_by('start_date')[:3]
    my_context = {'latest_events_list': latest_events_list}
    my_context.update(context)
    return render_to_response(template, my_context)

def direct_to_template(request, template):
    return enrich_and_render_to_response(template)