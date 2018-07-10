
from customerDetailsManagement.models import BankCustomer
from customerDetailsManagement.models import BankAccount
from customerDetailsManagement.models import CreditTransfer
from customerDetailsManagement.serializers import BankAccountSerializer
from customerDetailsManagement.serializers import BankCustomerSerializer
from customerDetailsManagement.serializers import CreditTransferSerializer

from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

'''  
    Bank Customer CRUD Views
'''

class BankCustomerList(generics.ListAPIView):
    queryset = BankCustomer.objects.all()
    serializer_class = BankCustomerSerializer

class BankCustomerCreate(APIView):
    def post(self, request, format=None):
        serializer = BankCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankCustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankCustomer.objects.all()
    serializer_class = BankCustomerSerializer


    '''  Bank Account CRUD Views'''


class BankAccountList(generics.ListAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class BankAccountCreate(APIView):
    def post(self, request, format=None):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

''' Return customer specific accounts '''

class CustomerBankAccount(APIView):
    def get(self, request , customer_id):
        try:
            accounts = BankAccount.objects.filter(customer_id=customer_id)
            serializer = BankAccountSerializer(accounts, many=True)
            return Response(serializer.data)
        except accounts.DoesNotExist:
            raise Http404


'''  Credit Transfer CRUD Views  (Ideally Delete should not be given for once submitted transfers)'''


class CreditTransferList(generics.ListAPIView):
    queryset = CreditTransfer.objects.all()
    serializer_class = CreditTransferSerializer

class CreditTransferCreate(APIView):
    def post(self, request, format=None):
        '''logging.debug("Oh hai!")
        print (request.data)

        logger.info(serializer.data.items());
        print("Customer id ",serializer.data.get("originator_customer_id"));
        print(serializer.data.get("originator_customer_id"));
        print(serializer.data.get("originator_acc_number"));'''
        serializer = CreditTransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreditTransferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditTransfer.objects.all()
    serializer_class = CreditTransferSerializer





