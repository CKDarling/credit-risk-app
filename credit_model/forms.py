from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from credit_model.models import Loan,City,State



class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['city','state','bank_state','term','number_emp','new_exist','urban_rural','disbursement_gross']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        if 'city' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')
