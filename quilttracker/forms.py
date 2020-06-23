from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Quilt, Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
        )
