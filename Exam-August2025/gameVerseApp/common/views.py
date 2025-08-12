from django.views.generic import TemplateView

from common.mixins import SingleObjectMixin


class IndexPage(SingleObjectMixin, TemplateView):
    template_name = "common/index.html"
