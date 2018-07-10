import logging
from .models import BankCustomer , BankAccount , CreditTransfer
from rest_framework import serializers

logger = logging.getLogger(__name__)
class BankCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCustomer
        fields = ('id','first_name', 'last_name', 'birth_date', 'address','coordinate')


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('customer_id', 'acc_number', 'acc_type', 'acc_balance')




class CreditTransferSerializer(serializers.ModelSerializer):

    def validate_originator_customer_id(self, originator_customer_id):
        """
        Check that Customer Id exists or not in Database
        """
        customer_id = BankCustomer.objects.filter(id=originator_customer_id)
        if customer_id.exists():
            return originator_customer_id;
        else:
            raise serializers.ValidationError("Customer doesn't exits , Please make sure you have passed the right customer id")

    def validate(self, data):
        """
        Check that account information of originator is correct
        Check that transfer amount is greater than zero and Customer have ssufficient balance to transfer
        """

        orig_account_number=data["originator_acc_number"]
        orig_customer_id=data["originator_customer_id"]
        account_details = BankAccount.objects.filter(acc_number=orig_account_number,customer_id=orig_customer_id)
        if account_details.exists():
            transfer_amount = data["transfer_amount"]
            avl_balance = BankAccount.objects.filter(acc_number=orig_account_number).values("acc_balance")[0]["acc_balance"]
            if transfer_amount > avl_balance:
                raise serializers.ValidationError("Transfer amount is more than available balance")
            elif transfer_amount <=0:
                logger.error("Amount to execute transfer is " + str(transfer_amount) + " that is less than zero")
                raise serializers.ValidationError("Amount to be transferred should be greater than zero")
            return data;
        else:
            raise serializers.ValidationError("customer & account are not linked")


    class Meta:
        model = CreditTransfer
        fields = ('id', 'originator_customer_id', 'originator_acc_number', 'transfer_amount','beneficiary_customer_id','beneficary_acc_number')

