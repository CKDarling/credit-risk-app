from django_tables2.utils import A
import django_tables2 as tables
from django.core.paginator import Paginator
from credit_model.models import Loan,City,State,FedChargeOff


class FedTable(tables.Table):
    DefaultRate = tables.Column(linkify=False)
    Year = tables.Column(linkify=False)
    Quarter = tables.Column(linkify=False)

    class Meta:
        model = FedChargeOff
        template_name = "credit_model/table.html"
        fields = ('DefaultRate','Year','Quarter')
