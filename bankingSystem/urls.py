from django.contrib import admin
from django.conf.urls import url, include

'''
Below url aptterns will redirect the request to respectiive app based on context in incoming request.
there are three possible context

    1. customer context will redirect request to context registered in customer.urls app
    2. account context will redirect to context registered in account.urls app
    3. payments context will redirect to context registered in payments.urls app
    
    for more detail please see the comment in respective app urls file (ex : customer.urls)
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'customer/', include('customer.urls')),
    url(r'account/', include('account.urls')),
    url(r'payment/', include('payments.urls')),
]

# {"originator_customer_id":5 ,"originator_acc_number":101, "transfer_amount":20,"beneficary_acc_number":5}
# {"first_name":"Test_manish" ,"last_name":"Jain", "address":"Jain Temple","birth_date":"1993-10-28"}
# {"customer_id":"1" ,"acc_number":"100", "acc_type":"credit_card","acc_balance":"34.5"}
