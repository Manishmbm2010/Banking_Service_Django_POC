import computed_property
from django.db import models
from geopy.geocoders import Nominatim
import computed_property

class BankCustomer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100);
    birth_date = models.DateField();
    address = models.CharField(max_length=1000);


    def __str__(self):
        return self.first_name+" "+self.last_name;

    @property
    def calculate_coordinates(self):
        geolocator = Nominatim()
        location = geolocator.geocode(self.address)
        #print(location.address)
        return (location.latitude, location.longitude)

    coordinate = computed_property.ComputedCharField(max_length=3 * 64, blank=True,compute_from='calculate_coordinates')

#{"first_name":"Manish1" ,"last_name":"Jain", "address":"Jain Temple","birth_date":"1993-10-28"}


class BankAccount(models.Model):
    customer_id = models.ForeignKey(BankCustomer, on_delete=models.CASCADE)
    acc_number = models.IntegerField(primary_key=True, max_length=20)
    acc_type = models.CharField(max_length=30)
    acc_balance = models.FloatField();
    def __str__(self):
        return self.customer_id;



#{"customer_id":"1" ,"acc_number":"100", "acc_type":"credit_card","acc_balance":"34.5"}


class CreditTransfer(models.Model):
    transfer_id = models.IntegerField(primary_key=True,auto_created=True)
    originator_customer_id = models.IntegerField();
    originator_acc_number = models.IntegerField();
    transfer_amount = models.FloatField();
    beneficiary_customer_id = models.IntegerField();
    beneficary_acc_number = models.IntegerField();

    def __str__(self):
        return self.transfer_id;

#{"originator_customer_id":"1" ,"originator_acc_number":"100", "transfer_amount":"credit_card","beneficiary_customer_id":"34.5","beneficary_acc_number":"5"}

