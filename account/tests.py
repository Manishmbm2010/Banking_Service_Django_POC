from rest_framework.test import APITestCase
from customer.models import BankCustomer
from .models import BankAccount


class BankAccountTestCase(APITestCase):

    def test_get_account_list(self):
        '''
        Test to verify that a get call for all account list return the success status
        '''
        response = self.client.get('/account/')
        self.assertEqual(200, response.status_code)

    def test_create_account(self):
        """
        Test to verify that a post call with valid account data
        """
        bankCustomer = BankCustomer(first_name="Manish", last_name="Jain", birth_date="1993-10-28",
                                    address="33,Rue du president,Ixelles")
        bankCustomer.save()

        data = {
            'customer_id': '1',
            'acc_type': 'Credit_Card',
            'acc_balance': '50',
        }
        response = self.client.post('/account/create', data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(data['customer_id'], str(response.data['customer_id']))
        self.assertEqual(data['acc_type'], response.data['acc_type'])
        self.assertEqual(float(data['acc_balance']), response.data['acc_balance'])

    def test_account_get(self):
        '''
        Test to verify that a get call for all account list return the success status
        '''
        bankCustomer = BankCustomer(first_name="Manish", last_name="Jain", birth_date="1993-10-28",
                                    address="33,Rue du president,Ixelles")
        bankCustomer.save()
        bankAccount = BankAccount(customer_id=bankCustomer, acc_type='Credit_Card', acc_balance=40.5)
        bankAccount.save()

        response = self.client.get('/account/'+str(bankAccount.acc_number))
        self.assertEqual(200, response.status_code)

    def test_account_update(self):
        """
               Test to verify the update of existing account details
        """
        bankCustomer = BankCustomer(first_name="Manish", last_name="Jain", birth_date="1993-10-28",
                                    address="33,Rue du president,Ixelles")
        bankCustomer.save()
        bankAccount = BankAccount(customer_id=bankCustomer, acc_type='Credit_Card', acc_balance=40.5)
        bankAccount.save()

        data = {
            'customer_id': '1',
            'acc_type': 'Credit_Card',
            'acc_balance': '50',
        }
        response = self.client.put('/account/'+str(bankAccount.acc_number), data, format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(data['customer_id'], str(response.data['customer_id']))
        self.assertEqual(data['acc_type'], response.data['acc_type'])
        self.assertEqual(float(data['acc_balance']), response.data['acc_balance'])


    def test_account_delete(self):
        """
               Test to verify the delete of existing account data
        """
        bankCustomer = BankCustomer(first_name="Manish", last_name="Jain", birth_date="1993-10-28",
                                    address="33,Rue du president,Ixelles")
        bankCustomer.save()
        bankAccount = BankAccount(customer_id=bankCustomer, acc_type='Credit_Card', acc_balance=40.5)
        bankAccount.save()

        response = self.client.delete('/account/'+str(bankAccount.acc_number))
        self.assertEqual(204, response.status_code)