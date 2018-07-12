from rest_framework.test import APITestCase
from customer.models import BankCustomer
from account.models import BankAccount
class CreditTransferTestCase(APITestCase):

    #def setUp(self):
        #, is_superuser=True
     #   User.objects.get(username="admin").delete()

    def test_get_credit_transfers(self):
        '''
        Test to verify that a get call for all credit transfers return the success status
        '''
        response = self.client.get('/payment/')
        self.assertEqual(200, response.status_code)

    def test_create_credit_transfer_with_validData(self):
        """
        Test to verify that a post call to create transfer with valid  data
        """
        bankCustomer = BankCustomer(first_name="Manish",last_name="Jain",birth_date="1993-10-28",address="33,Rue du president,Ixelles")
        bankCustomer.save()

        bankAccount = BankAccount(customer_id=bankCustomer,acc_number=120,acc_type='Credit_Card',acc_balance=40.5)
        bankAccount.save()

        data = {
            'originator_customer_id': bankCustomer.id,
            'originator_acc_number' : bankAccount.acc_number,
            'beneficary_acc_number': 500,
            'transfer_amount': 20.0
        }
        response= self.client.post('/payment/create',data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(data['originator_customer_id'],response.data['originator_customer_id'])
        self.assertEqual(data['originator_acc_number'], response.data['originator_acc_number'])
        self.assertEqual(data['transfer_amount'], response.data['transfer_amount'])


    def test_create_credit_transfer_with_more_transfer_amount(self):
        """
        Test to verify that a post call to create transfer with more amount than available balance.
        this is a negative test case
        """
        bankCustomer = BankCustomer(first_name="Manish",last_name="Jain",birth_date="1993-10-28",address="33,Rue du president,Ixelles")
        bankCustomer.save()

        bankAccount = BankAccount(customer_id=bankCustomer,acc_number=120,acc_type='Credit_Card',acc_balance=40.5)
        bankAccount.save()

        data = {
            'originator_customer_id': bankCustomer.id,
            'originator_acc_number' : bankAccount.acc_number,
            'beneficary_acc_number': 500,
            'transfer_amount': 50.0
        }
        response= self.client.post('/payment/create',data, format='json')
        self.assertEqual(400, response.status_code)