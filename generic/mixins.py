from django.views.generic.base import ContextMixin


class CategoryListMixing(ContextMixin):  # создает список категорий
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixing, self).get_context_data(**kwargs)  # переопределяем метод для формирования первоначальных данных
        context['current_url'] = self.request.path  # формирует текущий интернет адрес
        return context


