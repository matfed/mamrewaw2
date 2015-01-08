from datetime import datetime
from events.models import Event
from navigation.models import MenuEntry
from infoboxes.models import Infobox, Page

def path_prefix_adder(request):
    parts = filter(None,request.path_info.split('/'))
    if len(parts) > 0:
      return {'path_prefix': parts[0]}
    else:
      return {}

def menu_entries_adder(request):
    menu_entries = MenuEntry.objects.filter(parent__isnull=True).order_by('position')
#    for entry in menu_entries:
#        entry.check_if_selected(request.path_info)
    my_context = {'menu_entries': menu_entries}
    return my_context

def latest_events_adder(request):
    latest_events_list = Event.objects.filter(start_date__gte=datetime.now().date()).order_by('start_date')[:3]
    my_context = {'latest_events_list': latest_events_list}
    return my_context

def infoboxes_adder(request):
    try:
        # page = Page.objects.get(pk=request.path_info)
        # infoboxes = page.infobox_set.all()
	infoboxes = Infobox.objects.order_by('position')
        my_context = {'infoboxes': infoboxes}
        return my_context
    except Page.DoesNotExist:
        return {}
    
