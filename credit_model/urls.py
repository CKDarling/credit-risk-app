from django.contrib import admin
from django.urls import path
from credit_model.views import (landing_index,ProdModel,thanks_index,load_cities,about,FedDataView)
from django.conf.urls.static import static

app_name = 'credit_model'

urlpatterns = [
    path('',landing_index,name='landing_index'),
    path('model/',ProdModel.as_view(),name='model_input'),
    path('about/',about,name='about'),
    path('thanks/',thanks_index,name='thanks_index'),
    path('fed_data/',FedDataView.as_view(),name='fed_data'),
    path('ajax/load-cities/',load_cities, name='ajax_load_cities'),
]
