from customer.models import BankCustomer
from customer.serializers import BankCustomerSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging, logging.config
import bankingSystem

logger = logging.getLogger(__name__)


'''  
Bank Customer CRUD Views
'''

'''
This view return the list of all available customer in database
'''


class BankCustomerList(generics.ListAPIView):
    #logger.info("Call to list all the customers")
    queryset = BankCustomer.objects.all()
    serializer_class = BankCustomerSerializer


'''
Below view create the customer, accept the customer information from request and save to database if serilization is valid.
return 201 if customer created with full customer detials else 400 consider the incoming request as bad request.
'''


class BankCustomerCreate(APIView):
    def post(self, request, format=None):
        #logger.info("Call to create the customers")
        serializer = BankCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
From below view details of single customer can be retrieved , updated and deleted.
'''


class BankCustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankCustomer.objects.all()
    serializer_class = BankCustomerSerializer
