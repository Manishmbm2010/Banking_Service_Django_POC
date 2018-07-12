import logging
from django.db import models

logger = logging.getLogger(__name__)

'''
Credit transfer model has been designed to save the payments initiated by customers
It takes originator id , account number and perform a validation before saving the transfer to database
whether originator customer exists and it has account from which transaction is initiated
There are no check on beneficiary account number, because beneficiary can be from some other bank.
'''


class CreditTransfer(models.Model):
    originator_customer_id = models.IntegerField();
    originator_acc_number = models.IntegerField();
    transfer_amount = models.FloatField();
    beneficary_acc_number = models.IntegerField();

    '''
    Below function is used to show the transaction id in admin view
    '''

    def __str__(self):
        return self.id.__str__();
