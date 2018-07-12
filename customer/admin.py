from django.contrib import admin

from .models import BankCustomer

"""
Register Bank Customer Model for Admin functionalities 
So customer can be created ,deleted and Updated from Admin site (/admin)
"""
admin.site.register(BankCustomer)
