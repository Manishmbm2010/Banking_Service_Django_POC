from django.conf.urls import url
from payments import views
from rest_framework.urlpatterns import format_suffix_patterns

'''
Customer url 

r'create'               POST:   /payment/create    : new payment will be created from the post request data
r'^$'                   GET:    /payment           : will list all the payment
r'^(?P<pk>[0-9]+)/$'    GET:    /payment/1         : will give the details of payment whose id is 1
r'^(?P<pk>[0-9]+)/$'    PUT:    /payment/1         : payment whose id is 1 , details would be updated from request data
r'^(?P<pk>[0-9]+)/$'    DELETE: /payment/1         : payment whose id is 1 will be deleted from dtabase
'''


urlpatterns = [
    url(r'^$', views.CreditTransferList.as_view()),
    url(r'create', views.CreditTransferCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CreditTransferDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
