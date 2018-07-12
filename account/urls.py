from django.conf.urls import url
from account import views
from rest_framework.urlpatterns import format_suffix_patterns

'''
Account url 

r'create'               POST:   /account/create    : new account will be created from the post request data
r'^$'                   GET:    /account           : will list all the account
r'^(?P<pk>[0-9]+)$'    GET:    /account/1         : will give the details of account whose id is 1
r'^(?P<pk>[0-9]+)$'    PUT:    /account/1         : account whose id is 1 , details would be updated from request data
r'^(?P<pk>[0-9]+)$'    DELETE: /account/1         : account whose id is 1 will be deleted from dtabase

'^getCustomerAccount/(?P<customer_id>[0-9]+)/$' GET: account/getCustomerAccount/1 : all the account of customer whose id is 1 will be listed

'''


urlpatterns = [
    url(r'^$', views.BankAccountList.as_view()),
    url(r'create', views.BankAccountCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.BankAccountDetail.as_view()),
    url(r'^getCustomerAccount/(?P<customer_id>[0-9]+)/$', views.CustomerBankAccount.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
