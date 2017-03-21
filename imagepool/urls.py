from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required  # контроль за выполнение пользователем входа на сайт

from imagepool.views import get_list, upload_file, delete_file


urlpatterns = patterns('',
    url(r'^$', login_required(get_list), name='imagepool_index'),
    url(r'^upload/$', login_required(upload_file), name='imagepool_upload'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(delete_file), name='imagepool_delete'),
)
