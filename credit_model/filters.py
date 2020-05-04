from django_filters import FilterSet,NumberFilter,DateRangeFilter,DateFilter

from credit_model.models import FedChargeOff



class FedFilter(FilterSet):
    class Meta:
        model = FedChargeOff
        fields = {'DefaultRate': ['lt', 'gt'],
                  "Year": ["exact",],
                  "Quarter": ["exact"]
                  }
