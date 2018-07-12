import logging
from .models import BankCustomer
from rest_framework import serializers

logger = logging.getLogger(__name__)

'''
Serializer class is to serialize and deserialize the object.Convert the incoming request to model instance that can saved in 
database and convert the response from model instance to required output format like json.
Field is set to return only customer id, first_name , last_name birth_data , address and coordinate in response from BankCustomer model
'''


class BankCustomerSerializer(serializers.ModelSerializer):
    #logger.info("Serializing/Deserializing the customer objects")

    class Meta:
        model = BankCustomer
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'address', 'coordinate')
