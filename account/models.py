import logging
from django.db import models
from model_utils import Choices
from customer.models import BankCustomer

logger = logging.getLogger(__name__)

'''
Declaring Bank Account model , to store the Bank account details of customers.
account number would be primary key and since customer should exists in database , a foreign key 
relationship has been defined on customer id field with customer tables.
For Acc Type only two choice can be accepted.
No constraint has been implemented on Amount field because amount can zero , negative and positive.

'''


class BankAccount(models.Model):
    acc_number = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(BankCustomer, on_delete=models.CASCADE)
    acc_type = models.CharField(max_length=20, choices=Choices(('Credit_Card', 'Credit_Card'),
                                                               ('Debit_Card', 'Debit_Card')))
    acc_balance = models.FloatField();

    '''
       Below function is used to show the customer id in admin view
    '''

    def __str__(self):
        return self.customer_id.__str__();
