from goods.models import Good
from django.forms import ModelForm

class GoodForm(ModelForm):

    class Meta:
        model = Good

