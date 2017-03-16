from django.views.generic.base import ContextMixin


class CategoryListMixing(ContextMixin):  # создает список категорий

    def get_context_data(self, **kwargs):
        context = super(CategoryListMixing, self).get_context_data(**kwargs)  # переопределяем метод для формирования первоначальных данных
        context['current_url'] = self.request.path  # формирует текущий интернет адрес
        return context


class PageNumberMixin(CategoryListMixing):  # помещает номер страницы в особую переменную контекста данных

    def get_context_data(self, **kwargs):
        context = super(PageNumberMixin, self).get_context_data(**kwargs)
        try:
            context['pn'] = self.request.GET['page']
        except KeyError:
            context['pn'] = '1'
        return context
