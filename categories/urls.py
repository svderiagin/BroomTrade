from django.conf.urls import url, patterns

from django.contrib.auth.decorators import login_required
from categories.views import CategoriesEdit


urlpatterns = patterns('',
    url(r'^$', login_required(CategoriesEdit.as_view()), name='categories_edit'),
)

