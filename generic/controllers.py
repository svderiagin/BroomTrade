from django.views.generic.base import View


class PageNumberView(View):  # получает номер страницы и добавляет его к интернет-адресу переадресации после успешного сохранения или удаления записи

    def get(self, request, *args, **kwargs):  # сортировка
        try:
            self.sort = self.request.GET['sort']
        except KeyError:
            self.sort = '0'
        try:
            self.order = self.request.GET['order']
        except KeyError:
            self.order = 'A'
        return super(PageNumberView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET['page']
        except KeyError:
            pn = '1'
        self.success_url += '?page=' + pn
        return super(PageNumberView, self).post(request, *args, **kwargs)




