from django.views.generic.base import View


class PageNumberView(View):  # получает номер страницы и добавляет его к интернет-адресу переадресации после успешного сохранения или удаления записи

    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET['page']
        except KeyError:
            pn = '1'
        self.success_url += '?page=' + pn
        return super(PageNumberView, self).post(request, *args, **kwargs)



