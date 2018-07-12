import logging
from .models import CreditTransfer
from customer.models import BankCustomer
from account.models import BankAccount
from rest_framework import serializers

logger = logging.getLogger(__name__)

'''
Serializer class is to serialize and deserialize the object.Convert the incoming request to model instance that can saved in 
database and convert the response from model instance to required output format like json.
Field is set to return only customer 'id', 'originator_customer_id', 'originator_acc_number', 'transfer_amount',
'beneficary_acc_number' information from "credit_transfer" model
'''


class CreditTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditTransfer
        fields = ('id', 'originator_customer_id', 'originator_acc_number', 'transfer_amount', 'beneficary_acc_number')

    '''
    Below are validation before accepting the transfer and saving into database
    '''

    def validate_originator_customer_id(self, originator_customer_id):
        """
        Check that Customer Id exists or not in Database
        """
        customer_id = BankCustomer.objects.filter(id=originator_customer_id)
        if customer_id.exists():
            return originator_customer_id;
        else:
            raise serializers.ValidationError(
                "Customer doesn't exits , Please make sure you have passed the right customer id")

    def validate(self, data):
        '''
        Below validation check whether bank account is linked to originator customer id or not
        and transfer amount is greater than zero and not more than available balance in his account
        '''

        orig_account_number = data["originator_acc_number"]
        orig_customer_id = data["originator_customer_id"]
        account_details = BankAccount.objects.filter(acc_number=orig_account_number, customer_id=orig_customer_id)
        if account_details.exists():
            transfer_amount = data["transfer_amount"]
            avl_balance = BankAccount.objects.filter(acc_number=orig_account_number).values("acc_balance")[0][
                "acc_balance"]
            if transfer_amount > avl_balance:
                raise serializers.ValidationError("Transfer amount is more than available balance")
            elif transfer_amount <= 0:
                logger.error("Amount to execute transfer is " + str(transfer_amount) + " that is less than zero")
                raise serializers.ValidationError("Amount to be transferred should be greater than zero")
            return data;
        else:
            raise serializers.ValidationError("customer & account are not linked")
