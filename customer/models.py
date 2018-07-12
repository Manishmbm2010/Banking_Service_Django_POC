import logging
from django.db import models
from geopy.geocoders import Nominatim
import computed_property

logger = logging.getLogger(__name__)

'''
Customer model has been designed to store customer personal details.
customer id would be automatically created by django.
Customer address coordinates would be calculated before saving the objects details to database.
Any updated in address would recalculate the coordinates as well.
'''


class BankCustomer(models.Model):
    #logger.info("Model Called")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100);
    birth_date = models.DateField();
    address = models.CharField(max_length=1000);

    @property
    def calculate_coordinates(self):
        geolocator = Nominatim()
        location = geolocator.geocode(self.address)
        return (location.latitude, location.longitude)

    coordinate = computed_property.ComputedCharField(max_length=3 * 64, blank=True,
                                                     compute_from='calculate_coordinates')

    '''
           Below function is used to show the customer id in admin view
    '''

    def __str__(self):
        return str(self.id);
