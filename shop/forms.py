from django.forms import ModelForm
from shop.models import Order

class AppForm(ModelForm):
    class Meta:
        model = Order
        fields = ['pername','perphone', 'peremail']

    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields['pername'].widget.attrs['id'] = 'name'
        self.fields['pername'].widget.attrs['type'] = 'text'
        self.fields['pername'].widget.attrs['class'] = 'validate'
        self.fields['pername'].widget.attrs['placeholder'] = 'Имя'

        self.fields['perphone'].widget.attrs['id'] = 'phone'
        self.fields['perphone'].widget.attrs['type'] = 'text'
        self.fields['perphone'].widget.attrs['class'] = 'validate'

        self.fields['peremail'].widget.attrs['id'] = 'email'
        self.fields['peremail'].widget.attrs['type'] = 'email'
        self.fields['peremail'].widget.attrs['class'] = 'validate'