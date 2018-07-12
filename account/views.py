from account.models import BankAccount
from account.serializers import BankAccountSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

'''  Bank Account CRUD Views'''

'''
This view return the list of all available account in database
'''


class BankAccountList(generics.ListAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


'''
Below view create the account, accept the account information from request and save to database if serilization is valid.
return 201 if account created with full account detials else 400 consider the incoming request as bad request.
'''


class BankAccountCreate(APIView):
    def post(self, request, format=None):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
From below view details of single account can be retrieved , updated and deleted.
'''


class BankAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


''' 
Below view just return customer specific accounts 
'''


class CustomerBankAccount(APIView):
    def get(self, request, customer_id):
        try:
            accounts = BankAccount.objects.filter(customer_id=customer_id)
            serializer = BankAccountSerializer(accounts, many=True)
            return Response(serializer.data)
        except accounts.DoesNotExist:
            raise Http404
