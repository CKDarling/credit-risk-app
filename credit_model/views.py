from django.shortcuts import render
from django.conf import settings
from credit_model.tables import FedTable
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView,
                                  FormView)
from credit_model.forms import LoanForm
from credit_model.models import Loan,City,State,FedChargeOff
# from credit_model. import LoanForm
import pickle
import os
import pandas as pd
from django_tables2 import RequestConfig, SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from credit_model.filters import FedFilter


RFM_PATH = os.path.join(settings.DS_MODELS,'RandomForestModel.sav')
PROD_TEST_ROUTE = os.path.join(settings.DS_MODELS,'production_test.csv')
PROD_TRAIN_ROUTE = os.path.join(settings.DS_MODELS,'production_train.csv')

def landing_index(request):
    return render(request,'credit_model/landing_index.html')

def thanks_index(request):
    return render(request,'credit_model/thanks.html')

def about(request):
    return render(request,'credit_model/about.html')


class FedDataView(SingleTableMixin,FilterView):
   context_object_name = 'FedData'
   model = FedChargeOff
   table_class = FedTable
   filterset_class = FedFilter
   template_name='credit_model/fed_data.html'

def RfcModel(city_val,state_val,BankState,Term,NumberEmp,NewExist,UrbanRural,DisbursementGross):
    prod_test = pd.read_csv(PROD_TEST_ROUTE) # File Route
    prod_train = pd.read_csv(PROD_TRAIN_ROUTE) # File Route
    # Gather inputs and arrange them as a single row dataframe
    row_df = pd.DataFrame([pd.Series([city_val,state_val,BankState,Term,NumberEmp,NewExist,UrbanRural,DisbursementGross],index=prod_test.columns)])
    # Add production sets to new test data
    concat_df = pd.concat([prod_train,prod_test,row_df])
    # dummie all values possible with train, test, and production data
    feature_df = pd.get_dummies(concat_df)
    # Drop target variable from dataset
    feature_df.drop(['MIS_Status'], axis=1,inplace=True)
    # Gather the now dummies production values
    x = feature_df.iloc[[-1]].copy()
    # Read in model
    randomforest = pickle.load(open(RFM_PATH,'rb'))
    # Predict probability of loan default
    prediction = randomforest.predict_proba(x)
    # Return probability of default only
    return prediction[:,1] # Gathers the probability of default

class ProdModel(FormView):
    template_name = 'credit_model/model_index.html'
    form_class = LoanForm

    def post(self, request):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = LoanForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # Gathering cleaned values
                City = form.cleaned_data['city']
                City_val = City.name # Gathers the actual city name, not the unique ID
                State = form.cleaned_data['state']
                State_val = State.name # Gathers the actual state name, not the unique ID
                BankState = form.cleaned_data['bank_state']
                Term = form.cleaned_data['term']
                NumberEmp = form.cleaned_data['number_emp']
                NewExist = form.cleaned_data['new_exist']
                UrbanRural = form.cleaned_data['urban_rural']
                DisbursementGross = form.cleaned_data['disbursement_gross']
                # Input values into the model and return a probability of default
                loan_default_prob = RfcModel(City_val,State_val,BankState,Term,NumberEmp,NewExist,UrbanRural,DisbursementGross)
                # gather the values and their prediction value into a database
                model_insert = Loan(city=City,state=State,
                                    bank_state=BankState,
                                    term=Term,
                                    number_emp=NumberEmp,
                                    new_exist=NewExist,
                                    urban_rural=UrbanRural,
                                    disbursement_gross=DisbursementGross,
                                    prediction_prob=loan_default_prob)
                # Insert the values and their prediction value into a database
                model_insert.save()

                # Alter probability of default into front-end format.
                loan_default_prob = str(round(loan_default_prob[0]*100,4))+"%"
                # To ensure values are of adequate type and clean.
                # successful_model_post is 0 until reaching this point, then is altered to 1. This is utilized by javascript on the frontend.
                successful_model_post = 1
                return render(request, 'credit_model/thanks.html',{'prediction_value':loan_default_prob,
                                                                   'successful_model_post':successful_model_post,
                                                                   'City':City,
                                                                   'State':State,
                                                                   'BankState':BankState,
                                                                   'Term':Term,
                                                                   'NumberEmp':NumberEmp,
                                                                   'NewExist':NewExist,
                                                                   'UrbanRural':UrbanRural,
                                                                   'DisbursementGross':DisbursementGross})
            else:
                form = LoanForm()
                # To ensure values are of adequate type and clean.
                # successful_model_post is 0 until reaching this point, then is altered to 1. This is utilized by javascript on the frontend.
                successful_model_post = 0
                return render(request, 'credit_model/model_index.html',
                                        {'form': form,'invalid_model_input':'Invalid Model Input',
                                        'successful_model_post':successful_model_post})
        else:
            form = LoanForm()
            return render(request, 'credit_model/model_index.html', {'form': form})



def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'credit_model/city_dropdown_list_options.html', {'cities': cities})
