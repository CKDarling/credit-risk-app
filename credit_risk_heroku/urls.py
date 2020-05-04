from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'credit_risk_heroku'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('credit_model.urls',namespace='home')),
]
