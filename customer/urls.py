from django.conf.urls import url
from customer import views
from rest_framework.urlpatterns import format_suffix_patterns
'''
Customer url 

r'create'               POST:   /customer/create    : new customer will be created from the post request data
r'^$'                   GET:    /customer           : will list all the customers
r'^(?P<pk>[0-9]+)/$'    GET:    /customer/1         : will give the details of customer whose id is 1
r'^(?P<pk>[0-9]+)/$'    PUT:    /customer/1         : customer whose id is 1 , details would be updated from request data
r'^(?P<pk>[0-9]+)/$'    DELETE: /customer/1         : customer whose id is 1 will be deleted from dtabase
'''

urlpatterns = [
    url(r'^$', views.BankCustomerList.as_view()),
    url(r'create', views.BankCustomerCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BankCustomerDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
