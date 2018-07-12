import logging
from .models import BankAccount
from rest_framework import serializers

logger = logging.getLogger(__name__)


'''
Serializer class is to serialize and deserialize the object.Convert the incoming request to model instance that can saved in 
database and convert the response from model instance to required output format like json.
Field is set to return only customer id, account number,type and balance information from "BankAccount" model
'''


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('customer_id', 'acc_number', 'acc_type', 'acc_balance')
