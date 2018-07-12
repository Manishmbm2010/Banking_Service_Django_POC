from payments.models import CreditTransfer
from payments.serializers import CreditTransferSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging, logging.config
import bankingSystem

logger = logging.getLogger(__name__)
logging.config.dictConfig(bankingSystem.settings.LOGGING)

'''  
Credit Transfer CRUD Views  (Ideally Delete should not be given for once submitted transfers)
'''

'''
This view return the list of all payments in database
'''


class CreditTransferList(generics.ListAPIView):
    queryset = CreditTransfer.objects.all()
    serializer_class = CreditTransferSerializer


'''
Below view create the payments, accept the payments information from request and save to database if serilization is valid.
return 201 if payments created with full payments detials else 400 consider the incoming request as bad request.
'''


class CreditTransferCreate(APIView):
    def post(self, request, format=None):
        serializer = CreditTransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
From below view details of single payments can be retrieved , updated and deleted.
'''


class CreditTransferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditTransfer.objects.all()
    serializer_class = CreditTransferSerializer
