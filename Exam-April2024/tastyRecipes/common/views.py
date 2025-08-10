from django.shortcuts import render
from django.views.generic import TemplateView

from common.mixins import SingleObjectMixin


class HomePageView(SingleObjectMixin, TemplateView):
    template_name = 'common/home-page.html'
