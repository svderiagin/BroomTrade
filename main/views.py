from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixing


class MainPageView(TemplateView, CategoryListMixing):
    template_name = 'mainpage.html'

