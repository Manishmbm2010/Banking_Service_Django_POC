import logging
from django.db import models
from geopy.geocoders import Nominatim
import computed_property
from model_utils import Choices

logger = logging.getLogger(__name__)

class BankCustomer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100);
    birth_date = models.DateField();
    address = models.CharField(max_length=1000);

    def __str__(self):
        return str(self.id);

    @property
    def calculate_coordinates(self):
        geolocator = Nominatim()
        location = geolocator.geocode(self.address)
        return (location.latitude, location.longitude)

    coordinate = computed_property.ComputedCharField(max_length=3 * 64, blank=True,compute_from='calculate_coordinates')




class BankAccount(models.Model):

    acc_number = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(BankCustomer, on_delete=models.CASCADE)
    acc_type = models.CharField( max_length=20, choices= Choices(('Credit_Card','Credit_Card'),
                                ('Debit_Card','Debit_Card')))
    acc_balance = models.FloatField();
    def __str__(self):
        return self.customer_id.__str__();




class CreditTransfer(models.Model):
    #transfer_id = models.IntegerField(primary_key=True,auto_created=True)
    originator_customer_id = models.IntegerField();
    originator_acc_number = models.IntegerField();
    transfer_amount = models.FloatField();
    beneficiary_customer_id = models.IntegerField();
    beneficary_acc_number = models.IntegerField();

    def __str__(self):
        return self.id.__str__();
