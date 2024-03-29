from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy  # применяем данную функцию т.к. устанавливаем значение success_url непосредственно в класе (иначе исп reverse)
from django.contrib.messages.views import SuccessMessageMixin  # сообщение об успешном добавлении записи
from django.contrib import messages
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed

from generic.controllers import PageNumberView
from news.models import New
from generic.mixins import CategoryListMixin, PageNumberMixin



class NewsListView(ArchiveIndexView, CategoryListMixin):
    model = New
    date_field = 'posted'
    template_name = 'news_index.html'
    paginate_by = 2
    allow_empty = True
    allow_future = True


class NewDetailView(DetailView, PageNumberMixin):
    model = New
    template_name = 'new.html'



class NewCreate(SuccessMessageMixin, CreateView, CategoryListMixin):
    model = New
    template_name = 'new_add.html'
    success_url = reverse_lazy('news_index')
    success_message = 'Новость успешно добавлена'


class NewUpdate(SuccessMessageMixin, PageNumberView, UpdateView, PageNumberMixin):
    model = New
    template_name = 'new_edit.html'
    success_url = reverse_lazy('news_index')
    success_message = 'Новость успешно изменена'


class NewDelete(PageNumberView, DeleteView, PageNumberMixin):
    model = New
    template_name = 'new_delete.html'
    success_url = reverse_lazy('news_index')

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Новость успешно удалена')
        return super(NewDelete, self).post(request, *args, **kwargs)



class RssNewsListFeed(Feed):
    title = 'Новости сайта "Веник-Торг"'
    description = title
    link = reverse_lazy('news_index')

    def items(self):
        return New.objects.all()[0:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.posted

    def item_link(self, item):
        return reverse('news_detail', kwargs={'pk': item.pk})


class AtomNewsListFeed(RssNewsListFeed):
    feed_type = Atom1Feed
    subtitle = RssNewsListFeed.description
