from django.views.generic.base import ContextMixin
from django.views.generic.dates import ArchiveIndexView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from generic.mixins import CategoryListMixin
from generic.mixins import PageNumberMixin
from generic.controllers import PageNumberView
from blog.models import Blog
from blog.forms import BlogForm



class SearchMixin(ContextMixin):  # помещает значени search и tag в контекст данных шаблона
    search = ''
    tag = ''

    def get_context_data(self, **kwargs):
        context = super(SearchMixin, self).get_context_data(**kwargs)
        context['search'] = self.search
        context['tag'] = self.tag
        return context


class BlogListView(PageNumberView, ArchiveIndexView, SearchMixin, CategoryListMixin):
    model = Blog
    date_field = 'posted'
    template_name = 'blog_index.html'
    paginate_by = 2
    allow_empty = True
    allow_future = True

    def get_queryset(self):  # выполняем фильтрацию в зависимости от того, какие значения присутствуют в search или tag
        blog = super(BlogListView, self).get_queryset()  # получаем набор записей уже отсортированных по полю posted
        if self.search:
            blog = blog.filter(Q(title__contains=self.search) | Q(description__contains=self.search) | Q(content__contains=self.search))
        if self.tag:
            blog = blog.filter(tags__name=self.tag)
        return blog


class BlogDetailView(PageNumberView, DetailView, SearchMixin, PageNumberMixin):
    model = Blog
    template_name = 'blog.html'



class BlogCreate(SuccessMessageMixin, CreateView, CategoryListMixin):
    model = Blog
    template_name = 'blog_add.html'
    success_url = reverse_lazy('blog_index')
    success_message = 'Статья успешно создана'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate, self).form_valid(form)


class BlogUpdate(PageNumberView, TemplateView, SearchMixin, PageNumberMixin):
    blog = None
    template_name = 'blog_edit.html'
    form = None

    def get(self, request, *args, **kwargs):
        self.blog = Blog.objects.get(pk=self.kwargs['pk'])
        if self.blog.user == request.user or request.user.is_superuser:
            self.form = BlogForm(instance=self.blog)
            return super(BlogUpdate, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))

    def get_context_data(self, **kwargs):
        context = super(BlogUpdate, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.blog = Blog.objects.get(pk=self.kwargs['pk'])
        if self.blog.user == request.user or request.user.is_superuser:
            self.form = BlogForm(request.POST, instance=self.blog)
            if self.form.is_valid():
                self.form.save()
                messages.add_message(request, messages.SUCCESS, 'Статья успешно изменена')
                redirect_url = reverse('blog_index') + '?page=' + self.request.GET['page']
                try:
                    redirect_url = redirect_url + '&search=' + self.request.GET['search']
                except KeyError:
                    pass
                try:
                    redirect_url = redirect_url = '&tag=' + self.request.GET['tag']
                except KeyError:
                    pass
                return redirect(redirect_url)
            else:
                return super(BlogUpdate, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))


class BlogDelete(PageNumberView, TemplateView, SearchMixin, PageNumberMixin):
    blog = None
    template_name = 'blog_delete.html'

    def get(self, request, *args, **kwargs):
        self.blog = Blog.objects.get(pk=self.kwargs['pk'])
        if self.blog.user == request.user or request.user.is_superuser:
            return super(BlogDelete, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))

    def get_context_data(self, **kwargs):
        context = super(BlogDelete, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context

    def post(self, request, *args, **kwargs):
        self.blog = Blog.objects.get(pk=self.kwargs['pk'])
        if self.blog.user == request.user or request.user.is_superuser:
            self.blog.delete()
            messages.add_message(request, messages.SUCCESS, 'Статья успешно удалена')
            redirect_url = reverse('blog_index') + '?page=' + self.request.GET['page']
            try:
                redirect_url = redirect_url + '&search=' + self.request.GET['search']
            except KeyError:
                pass
            try:
                redirect_url = redirect_url + '&tag=' + self.request.GET['tag']
            except KeyError:
                pass
            return redirect(redirect_url)
        else:
            return redirect(reverse('login'))
