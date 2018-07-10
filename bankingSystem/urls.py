"""bankingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from customerDetailsManagement import views

urlpatterns = [
    url(r'^getAllCustomers/$', views.BankCustomerList.as_view()),
    url(r'^createCustomer/$', views.BankCustomerCreate.as_view()),
    url(r'^getCustomerById/(?P<pk>[0-9]+)/$', views.BankCustomerDetail.as_view()),
    url(r'^getAllAccounts/$', views.BankAccountList.as_view()),
    url(r'^createAccount/$', views.BankAccountCreate.as_view()),
    url(r'^getAccountById/(?P<pk>[0-9]+)/$', views.BankAccountDetail.as_view()),
    url(r'^getCustomerAccount/(?P<customer_id>[0-9]+)/$', views.CustomerBankAccount.as_view()),
    url(r'^getAllCreditTransfers/$', views.CreditTransferList.as_view()),
    url(r'^createCreditTransfer/$', views.CreditTransferCreate.as_view()),
    url(r'^getCreditTransferById/(?P<pk>[0-9]+)/$', views.CreditTransferDetail.as_view()),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)


#http://localhost:8000/getAllCustomers/

#{"originator_customer_id":5 ,"originator_acc_number":101, "transfer_amount":81,"beneficiary_customer_id":34,"beneficary_acc_number":5}

#{"first_name":"Manish1" ,"last_name":"Jain", "address":"Jain Temple","birth_date":"1993-10-28"}

#{"customer_id":"1" ,"acc_number":"100", "acc_type":"credit_card","acc_balance":"34.5"}
