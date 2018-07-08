from .models import BankCustomer , BankAccount , CreditTransfer
from rest_framework import serializers

class BankCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCustomer
        fields = ('id','first_name', 'last_name', 'birth_date', 'address','coordinate')


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('customer_id', 'acc_number', 'acc_type', 'acc_balance')


class CreditTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditTransfer
        fields = ('transfer_id', 'originator_customer_id', 'originator_acc_number', 'transfer_amount','beneficiary_customer_id','beneficary_acc_number')