from django.views.generic import TemplateView, ListView
from eventiumApp.utils import get_user_obj
from events.models import Event


class IndexPage(TemplateView):
    template_name = "common/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizer_profile = get_user_obj()
        context['has_organizer_profile'] = bool(organizer_profile)
        return context


class EventsListView(ListView):
    model = Event
    template_name = 'common/events.html'
    context_object_name = 'events'
    ordering = ['-start_time']
