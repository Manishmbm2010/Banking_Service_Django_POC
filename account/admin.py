from django.contrib import admin

from .models import BankAccount

"""
Register Bank Account Model for Admin functionalities 
So Bank account can be created ,deleted and Updated from Admin site (/admin)
"""
admin.site.register(BankAccount)
