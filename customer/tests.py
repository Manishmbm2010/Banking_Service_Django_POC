from rest_framework.test import APITestCase

class BankCustomerTestCase(APITestCase):

    def test_get_customer_list(self):
        '''
        Test to verify that a get call for all customer return the success status
        '''
        response = self.client.get('/customer/')
        self.assertEqual(200, response.status_code)

    def test_customer_create(self):
        """
        Test to verify that a post call with valid Customer data
        """
        data = {
            'first_name': 'Test_Manish',
            'last_name' : 'Jain',
            'address': '33,Rue du president,Ixelles',
            'birth_date': '1993-10-28',
        }
        response= self.client.post('/customer/create',data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(data['first_name'],response.data['first_name'])
        self.assertEqual(data['last_name'], response.data['last_name'])
        self.assertEqual(data['address'], response.data['address'])
        self.assertEqual(data['birth_date'], response.data['birth_date'])

