from datetime import datetime
from events.models import Event
from navigation.models import MenuEntry
from django.shortcuts import render_to_response

def enrich_and_render_to_response(request, template, context = {}):
    latest_events_list = Event.objects.filter(start_date__gte=datetime.now().date()).order_by('start_date')[:3]
    menu_entries = MenuEntry.objects.order_by('position')
    for entry in menu_entries:
        entry.check_if_selected(request.path_info)
    my_context = {'menu_entries': menu_entries, 'latest_events_list': latest_events_list}
    my_context.update(context)
    return render_to_response(template, my_context)

def direct_to_template(request, template):
    return enrich_and_render_to_response(request, template)